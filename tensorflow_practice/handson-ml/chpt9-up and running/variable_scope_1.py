import tensorflow as tf

n_features = 3


# [1] painful to pass `threshold` as a parameter to the function for sharing variable.
def relu(X):
    # [1] this will raise an exception `Variable relu/threshold already exists`
    # with tf.variable_scope("relu"):

    # [2]
    with tf.variable_scope("relu", reuse=True):
        # [1]
        # threshold = tf.get_variable("threshold", shape=(), initializer=tf.constant_initializer(0.))

        # [2] raise an exception `Variable relu/threshold does not exist`
        threshold = tf.get_variable("threshold")

        w_shape = (int(X.get_shape()[1]), 1)
        print('w.shape: ', w_shape)
        w = tf.Variable(tf.random_normal(w_shape), name="weights")
        b = tf.Variable(0.0, name="bias")
        z = tf.add(tf.matmul(X, w), b, name="z")
        return tf.maximum(z, threshold, name="max")


X = tf.placeholder(tf.float32, shape=(None, n_features), name="X")
relus = [relu(X) for x in range(5)]
output = tf.add_n(relus, name="output")

train_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)

print(train_vars)

"""
train_vars = [   

]
"""
