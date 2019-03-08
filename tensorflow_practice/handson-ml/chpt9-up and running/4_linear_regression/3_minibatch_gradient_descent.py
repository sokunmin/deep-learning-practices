import numpy as np
import tensorflow as tf
from data.housing_data import *
from utils.tf_utils import *


def placeholder_example():
    A = tf.placeholder(tf.float32, shape=(None, 3))
    B = A * 2

    with tf.Session() as sess:
        B_val_1 = B.eval(feed_dict={
            A: [[1, 2, 3]]
        })
        B_val_2 = B.eval(feed_dict={
            A: [[4, 5, 6], [7, 8, 9]]
        })

        print(B_val_1)
        print(B_val_2)


def fetch_batch(epoch, n_batches, batch_index, batch_size):
    np.random.seed(epoch * n_batches + batch_index)  # not shown in the book
    indices = np.random.randint(m, size=batch_size)  # not shown in the book
    X_batch = scaled_housing_data_plus_bias[indices] # not shown in the book
    y_batch = housing.target.reshape(-1, 1)[indices]
    return X_batch, y_batch


def minibatch_gradient_descent():
    n_epochs = 1000
    learning_rate = 0.01
    X = tf.placeholder(tf.float32, shape=(None, n + 1), name='X')
    y = tf.placeholder(tf.float32, shape=(None, 1), name='X')

    theta = tf.Variable(tf.random_uniform([n + 1, 1], -1.0, 1.0, seed=42), name='theta')
    y_pred = tf.matmul(X, theta, name='predictions')
    error = y_pred - y

    mse = tf.reduce_mean(tf.square(error), name="mse")
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    training_op = optimizer.minimize(mse)

    init = tf.global_variables_initializer()

    # --------------------------------
    n_epochs = 10
    batch_size = 100
    n_batches = int(np.ceil(m / batch_size))

    with tf.Session() as sess:
        sess.run(init)

        for epoch in range(n_epochs):
            for batch_index in range(n_batches):
                X_batch, y_batch = fetch_batch(epoch, batch_index, batch_size)
                sess.run(training_op, feed_dict={X: X_batch, y: y_batch})
        best_theta = theta.eval()
        print(best_theta)


if __name__ == '__main__':
    tf.enable_eager_execution()
    minibatch_gradient_descent()

