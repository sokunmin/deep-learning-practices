import tensorflow as tf

from data.housing_data import *


# this is now shown in the book


def save_and_restore(n_epochs, learning_rate):
    X = tf.constant(scaled_housing_data_plus_bias, dtype=tf.float32, name='X')
    y = tf.constant(housing.target.reshape(-1, 1), dtype=tf.float32, name='y')

    theta = tf.Variable(tf.random_uniform([n + 1, 1], -1.0, 1.0, seed=42), name='theta')
    y_pred = tf.matmul(X, theta, name='predictions')

    error = y_pred - y

    mse = tf.reduce_mean(tf.square(error), name="mse")

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)

    training_op = optimizer.minimize(mse)

    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init)

        for epoch in range(n_epochs):
            if epoch % 100 == 0:
                print(f'Epoch {epoch}, MSE = {mse.eval()}')
                save_path = saver.save(sess, '/tmp/my_model.ckpt')
            sess.run(training_op)
        best_theta = theta.eval()
        save_path = saver.save(sess, '/tmp/my_model_final.ckpt')
        print(f'Best Θ = {best_theta}')

    # ---------- restore model ---------- #
    with tf.Session() as sess:
        saver.restore(sess, save_path)
        best_theta_restored = theta.eval()

    # Using a saver to load and restore `theta` with a different name, such as `weights`.
    saver = tf.train.Saver({'weights': theta})
    return best_theta, best_theta_restored


def restore_graph_state():
    """
        By default the saver also saves the graph structure itself in a second file with
        extension .meta. You can use the function `tf.train.import_meta_graph()` to restore
        the graph structure.

        This function loads the graph into the default graph and returns a `Saver` that can
        then be used to restore the graph state (i.e., the variable values):

        You can import a pretrained model without having to have the corresponding Python code
        to build the graph. This is very handy when you keep tweaking and saving your model:
        you can load a previously saved model without having to search for the version of the
         code that built it.

    """
    saver = tf.train.import_meta_graph('/tmp/my_model_final.ckpt.meta')  # loads graph structure
    theta = tf.get_default_graph().get_tensor_by_name('theta:0')

    with tf.Session() as sess:
        saver.restore(sess, '/tmp/my_model_final.ckpt')  # restores graph's state

        best_theta_restored = theta.eval()
        print(best_theta_restored)

    return best_theta_restored


if __name__ == '__main__':
    n_epochs = 1000
    learning_rate = 0.01

    best_theta, best_theta_restored = save_and_restore(n_epochs, learning_rate)
    print(np.allclose(best_theta, best_theta_restored))

    best_theta_restored = restore_graph_state()
    print(np.allclose(best_theta, best_theta_restored))
