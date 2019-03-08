import keras
import tensorflow as tf
import pandas as pd
from keras import layers
from keras.layers import Input, Concatenate

# df = pd.read_csv('movie.csv')
df = pd.read_csv('dataset/rating.csv')
print('userId.max: {:,}'.format(df.userId.max()))
print('movieId.max: {:,}'.format(df.movieId.max()))
movies = pd.read_csv('dataset/movie.csv')

HIDDEN_UNITS = (32, 4)
MOVIE_EMBEDDING_SIZE = 8
USER_EMBEDDING_SIZE = 8

# Each instance will consist of two inputs: a single user id, and a single movie id
user_id_input = Input(shape=(1,), name='user_id')
movie_id_input = Input(shape=(1,), name='movie_id')

user_embedded = layers.Embedding(input_dim=df.userId.max() + 1,
                                 output_dim=USER_EMBEDDING_SIZE,
                                 input_length=1,
                                 name='user_embedding')(user_id_input)

movie_embedded = layers.Embedding(input_dim=df.movieId.max() + 1,
                                  output_dim=MOVIE_EMBEDDING_SIZE,
                                  input_length=1,
                                  name='movie_embedding')(movie_id_input)

# Concatenate the embeddings (and remove the useless extra dimension)
concatenated = Concatenate()([user_embedded, movie_embedded])

out = layers.Flatten()(concatenated)

# Add one or more hidden layers
for n_hidden in HIDDEN_UNITS:
    out = layers.Dense(n_hidden, activation='relu')(out)

# A single output: our predicted rating
out = layers.Dense(1, activation='linear', name='prediction')(out)

model = keras.Model(
    inputs=[user_id_input, movie_id_input],
    outputs=out
)

model.summary(line_length=88)

model.compile(
    # Technical note: when using embedding layers, I highly recommend using one of the optimizers
    # found  in tf.train: https://www.tensorflow.org/api_guides/python/train#Optimizers
    # Passing in a string like 'adam' or 'SGD' will load one of keras's optimizers (found under
    # tf.keras.optimizers). They seem to be much slower on problems like this, because they
    # don't efficiently handle sparse gradient updates.
    tf.train.AdamOptimizer(0.005),
    loss='MSE',
    metrics=['MAE'],
)

history = model.fit(
    [df.userId, df.movieId],
    df.y,
    batch_size=5000,
    epochs=50,
    verbose=0,
    validation_split=0.5
)

# ----------- evaluation -----------
candidate_movies = movies[
    movies.title.str.contains('Naked Gun')
    | (movies.title == 'The Sisterhood of the Traveling Pants')
    | (movies.title == 'Lilo & Stitch')
].copy()

preds = model.predict([
    [uid] * len(candidate_movies), # User ids
    candidate_movies.index, # Movie ids
])

# NB: Remember we trained on 'y', which was a version of the rating column centered on 0. To translate
# our model's output values to the original [0.5, 5] star rating scale, we need to 'uncenter' the
# values, by adding the mean back
row = df.iloc[0] # The difference between rating and y will be the same for all rows, so we can just use the first
y_delta = row.rating - row.y
candidate_movies['predicted_rating'] = preds + y_delta

# Add a column with the difference between our predicted rating (for this user) and the movie's
# overall average rating across all users in the dataset.
candidate_movies['delta'] = candidate_movies['predicted_rating'] - candidate_movies['mean_rating']
candidate_movies.sort_values(by='delta', ascending=False)