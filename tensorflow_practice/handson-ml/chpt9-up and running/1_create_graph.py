from __future__ import division, print_function, unicode_literals

import tensorflow as tf

from utils.tf_utils import reset_graph
import sys
import inspect

reset_graph()


if __name__ == '__main__':
    x = tf.Variable(3, name='x')
    y = tf.Variable(4, name='y')
    f = x * x * y + y + 2
    print('[1]', inspect.currentframe().f_code.co_name)
    print(f)

    # [1-1]
    sess = tf.Session()
    sess.run(x.initializer)
    sess.run(y.initializer)
    result = sess.run(f)
    print('[1-1] ', result)

    # [1-2] with block
    with tf.Session() as sess:
        sess.run(x.initializer)
        sess.run(y.initializer)
        result = sess.run(f)
        print('[1-2] ', result)

    # [1-3]
    with tf.Session() as sess:
        x.initializer.run()  # => tf.get_default_session().run(x.initializer)
        y.initializer.run()
        result = f.eval()  # => tf.get_default_session().run(f)
        print('[1-3] ', result)

    # [1-4]
    init = tf.global_variables_initializer()  # prepare an init node
    with tf.Session() as sess:
        init.run()  # actually initialize all the variables
        result = f.eval()
        print('[1-4] ', result)

    # [1-5] Interactive Session
    init = tf.global_variables_initializer()  # prepare an init node
    sess = tf.InteractiveSession()
    init.run()
    result = f.eval()
    print('[1-5] ', result)
    sess.close()
