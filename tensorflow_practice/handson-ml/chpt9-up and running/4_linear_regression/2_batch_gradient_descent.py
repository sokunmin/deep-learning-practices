import tensorflow as tf

from data.housing_data import *


def run_with_sklearn():
    print('[sklearn-1] ', scaled_housing_data_plus_bias.mean(axis=0))
    print('[sklearn-2] ', scaled_housing_data_plus_bias.mean(axis=1))
    print('[sklearn-3] ', scaled_housing_data_plus_bias.mean())
    print('[sklearn-4] ', scaled_housing_data_plus_bias.shape)


def run_with_tensorflow():
    n_epochs = 1000
    learning_rate = 0.01

    X = tf.constant(scaled_housing_data_plus_bias,
                    dtype=tf.float32,
                    name='x')
    # housing.target is 1D array, we reshape it to a column vector,
    # where -1 means `unspecified` for one of the dimesions:
    # that dimension will be coputed based on the array's length and
    # the remaining dimensions.
    y = tf.constant(housing.target.reshape(-1, 1),
                    dtype=tf.float32,
                    name='y')

    theta = tf.Variable(tf.random_uniform([n + 1, 1], -1.0, 1.0),
                        name="theta")
    y_pred = tf.matmul(X,
                       theta,
                       name="predictions")
    error = y_pred - y
    mse = tf.reduce_mean(tf.square(error),
                         name="mse")
    # --------------------- gradients ---------------------- #
    # [gradient-1] compute manually
    # gradients = 2 / m * tf.matmul(tf.transpose(X), error)

    # [gradient-2] autodiff feature
    gradients = tf.gradients(mse, [theta])[0]

    # --------------------- optimizer ---------------------- #
    # [optimizer-1] compute manually
    # training_op = tf.assign(theta, theta - learning_rate * gradients)

    # [optimizer-2] built-in optimizer
    # optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    # training_op = optimizer.minimize(mse)

    # [optimizer-3] change optimizer to Momentum
    optimizer = tf.train.MomentumOptimizer(learning_rate=learning_rate,
                                           momentum=0.9)
    training_op = optimizer.minimize(mse)

    # --------------------- tf.Session() ---------------------- #
    init = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init)

        for epoch in range(n_epochs):
            if epoch % 100 == 0:
                print(f'Epoch={epoch}, MSE={mse.eval()}')
            sess.run(training_op)
        best_theta = theta.eval()
        print(best_theta)


def my_func_with_numpy(a, b):
    z = 0
    for i in range(100):
        z = a * b * np.cos(z + i) + z * np.sin(b - i)
    return z


def my_func_with_tensorflow():
    a = tf.Variable(0.2, name='a')
    b = tf.Variable(0.3, name='b')
    z = tf.constant(0.0, name='z0')
    for i in range(100):
        z = a * tf.cos(z + i) + z * tf.sin(b - i)

    grads = tf.gradients(z, [a, b])
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        init.run()
        print(z.eval())
        print(sess.run(grads))


if __name__ == '__main__':
    my_func_with_numpy(0.2, 0.3)
    my_func_with_tensorflow()
    run_with_sklearn()
    run_with_tensorflow()