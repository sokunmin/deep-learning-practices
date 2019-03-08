from keras import Input, layers
MOVIE_EMBEDDING_SIZE = USER_EMBEDDING_SIZE = 8

# Each instance consists of two inputs: a single user id, and a single movie id
user_id_input = Input(shape=(1,), name='user_id')
movie_id_input = Input(shape=(1,), name='movie_id')
user_embedded = layers.Embedding(df.userId.max() + 1, USER_EMBEDDING_SIZE,
                                       input_length=1, name='user_embedding')(user_id_input)
movie_embedded = layers.Embedding(df.movieId.max() + 1, MOVIE_EMBEDDING_SIZE,
                                        input_length=1, name='movie_embedding')(movie_id_input)

dotted = keras.layers.Dot(2)([user_embedded, movie_embedded])
out = keras.layers.Flatten()(dotted)

model = keras.Model(
    inputs = [user_id_input, movie_id_input],
    outputs = out,
)
model.compile(
    tf.train.AdamOptimizer(0.001),
    loss='MSE',
    metrics=['MAE'],
)
model.summary(line_length=88)