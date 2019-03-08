import tensorflow as tf

n_features = 3


def relu(X):
    w_shape = (int(X.get_shape()[1]), 1)
    print('w.shape: ', w_shape)
    w = tf.Variable(tf.random_normal(w_shape), name="weights")
    b = tf.Variable(0.0, name="bias")
    z = tf.add(tf.matmul(X, w), b, name="z")
    return tf.maximum(z, 0.0, name="relu")


X = tf.placeholder(tf.float32, shape=(None, n_features), name="X")
relus = [relu(X) for x in range(5)]
output = tf.add_n(relus, name="output")

train_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)

print(train_vars)

"""
train_vars = [   
    <tf.Variable 'weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'weights_1:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'bias_1:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'weights_2:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'bias_2:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'weights_3:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'bias_3:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'weights_4:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'bias_4:0' shape=() dtype=float32_ref>
]
"""
# TODO: get a collection of ops
tf.reset_default_graph()
graph = tf.Graph()

with graph.as_default():
    update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
    print(update_ops)
