import tensorflow as tf
from data.housing_data import *


def run_with_tensorflow():
    X = tf.constant(housing_data_plus_bias,
                    dtype=tf.float32,
                    name='x')
    # housing.target is 1D array, we reshape it to a column vector,
    # where -1 means `unspecified` for one of the dimesions:
    # that dimension will be coputed based on the array's length and
    # the remaining dimensions.
    y = tf.constant(housing.target.reshape(-1, 1),
                    dtype=tf.float32,
                    name='y')
    # CAUTION: cache `X.T`, which make codes run effectively.
    XT = tf.transpose(X)
    # Θ = (X^T．X)^(-1)．X^T．y
    theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT, X)), XT), y)

    with tf.Session() as sess:
        theta_value = theta.eval()
        print('[tensorflow] ', theta_value)


def run_with_numpy():
    X = housing_data_plus_bias
    y = housing.target.reshape(-1, 1)
    # Θ = (X^T．X)^(-1)．X^T．y
    theta_numpy = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

    print('[numpy] ', theta_numpy)


if __name__ == '__main__':
    run_with_tensorflow()
    run_with_numpy()