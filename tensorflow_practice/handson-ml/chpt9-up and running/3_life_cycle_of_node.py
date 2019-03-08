import tensorflow as tf

import time
"""
In single-process TensorFlow, multiple sessions do not share any state, 
even if they reuse the same graph (each session would have its own copy 
of every variable). 

In distributed TensorFlow, variable state is stored on the servers, 
not in the sessions, so multiple sessions can share the same variables.
"""

w = tf.constant(3)
x = w + 2
y = x + 5
z = x * 3


def method1():
    """
        All node values are dropped between graph runs,
        except variable values, which are maintained by
        the session across graph runs (queues and readers
        also maintain some state.)

        A variable starts its life when its initializer is run,
        and it ends when the session is closed.
    """
    start = time.time()
    with tf.Session() as sess:
        print('[1-1] ', y.eval())
        print('[1-2] ', z.eval())

    end = time.time()
    print('[1-3] elapsed: ', end - start)


def method2():
    start = time.time()
    with tf.Session() as sess:
        # evaluate both y and z in just one graph run.
        y_val, z_val = sess.run([y, z])
        print('[2-1] ', y_val)
        print('[2-1] ', z_val)
    end = time.time()
    print('[2-3] elapsed: ', end - start)


if __name__ == '__main__':
    method1()
    method2()
