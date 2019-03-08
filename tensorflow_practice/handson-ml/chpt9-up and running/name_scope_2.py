import tensorflow as tf

n_features = 3


# [1] painful to pass `threshold` as a parameter to the function for sharing variable.
def relu(X):
    with tf.name_scope("relu"):
        if not hasattr(relu, "threshold"):
            relu.threshold = tf.Variable(0., name="threshold")
        w_shape = (int(X.get_shape()[1]), 1)
        print('w.shape: ', w_shape)
        w = tf.Variable(tf.random_normal(w_shape), name="weights")
        b = tf.Variable(0.0, name="bias")
        z = tf.add(tf.matmul(X, w), b, name="z")
        return tf.maximum(z, relu.threshold, name="relu")


# decalre variable outside of the scope.
# threshold = tf.Variable(0., name="threshold")

X = tf.placeholder(tf.float32, shape=(None, n_features), name="X")
relus = [relu(X) for x in range(5)]
output = tf.add_n(relus, name="output")

train_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)

print(train_vars)

"""
train_vars = [   
    ---- declare variable outside of scope & pass it to the function ---- 
    <tf.Variable 'threshold:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu/bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu_1/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_1/bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu_2/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_2/bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu_3/weights:0' shape=(3, 1) dtype=float32_ref>,
    <tf.Variable 'relu_3/bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu_4/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_4/bias:0' shape=() dtype=float32_ref>
    
    ---- declare variable within the scope 
    <tf.Variable 'relu/threshold:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu/bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu_1/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_1/bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu_2/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_2/bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu_3/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_3/bias:0' shape=() dtype=float32_ref>, 
    <tf.Variable 'relu_4/weights:0' shape=(3, 1) dtype=float32_ref>, 
    <tf.Variable 'relu_4/bias:0' shape=() dtype=float32_ref>

]
"""
