import tensorflow as tf

from utils.tf_utils import reset_graph

reset_graph()


def method1():
    # add any node to the default graph automatically.
    x1 = tf.Variable(1)
    print('[1]] ', x1.graph is tf.get_default_graph())  # True


def method2():
    graph = tf.Graph()
    with graph.as_default():
        x2 = tf.Variable(2)
    print('[2-1] ', x2.graph is graph)  # True
    print('[2-2] ', x2.graph is tf.get_default_graph())  # False


if __name__ == '__main__':
    method1()
    print()
    method2()
