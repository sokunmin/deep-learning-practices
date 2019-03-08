# Backprop: http://www.claudiobellei.com/2018/01/06/backprop-word2vec/
# Implementation: http://www.claudiobellei.com/2018/01/07/backprop-word2vec-python/

import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.utils import np_utils
import tensorflow as tf


def tokenized(corpus):
    # TODO: convert to lower case
    # TODO: convert to lower case
    pass


def tokenize(corpus):
    """
    Tokenize the corpus text.
    # Arguments
        corpus: list containing a string of text
            (example: ["I like playing football with my friends"])
        corpus_tokenized: indexed list of words in the corpus,
            in the same order as the original corpus (the example above
            would return [[1, 2, 3, 4]])
    # Returns
        V: size of vocabulary
    """
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(corpus)
    corpus_tokenized = tokenizer.texts_to_sequences(corpus)
    V = len(tokenizer.word_index)
    return corpus_tokenized, V


def to_categorical(y, num_classes=None):
    """
    Converts a class vector (integers) to binary class matrix.
    E.g. for use with categorical_crossentropy.
    # Arguments
        y: class vector to be converted into a matrix
            (integers from 0 to num_classes).
        num_classes: total number of classes.
    # Returns
        A binary matrix representation of the input.
    """
    y = np.array(y, dtype='int')
    input_shape = y.shape
    if input_shape and input_shape[-1] == 1 and len(input_shape) > 1:
        input_shape = tuple(input_shape[:-1])
    y = y.ravel()
    if not num_classes:
        num_classes = np.max(y) + 1
    n = y.shape[0]
    categorical = np.zeros((n, num_classes))
    categorical[np.arange(n), y] = 1
    output_shape = input_shape + (num_classes,)
    categorical = np.reshape(categorical, output_shape)
    return categorical


def corpus2io(corpus_tokenized, V, window_size):
    """
    Converts/Maps corpus text into context and center words
    # Arguments
        corpus_tokenized: corpus text
        window_size: size of context window
    # Returns
        context and center words (arrays)
        Word2vec, which is developed by Google, is one of the famous state-of-the-art algorithm.
        4          5    1     6     7    8      1   9  2   3   10      11  2   3  12      13
    """
    for words in corpus_tokenized:
        L = len(words)
        for index, word in enumerate(words):
            contexts = []
            labels = []
            s = index - window_size
            e = index + window_size + 1

            # turn to one-hot encoder for vocaburary.
            contexts.append([words[i] - 1 for i in range(s, e) if 0 <= i < L and i != index])
            labels.append(word - 1)
            x = np_utils.to_categorical(contexts, V)
            y = np_utils.to_categorical(labels, V)
            yield (x, y.ravel())


def softmax(x):
    """
    Calculate softmax based probability for given input vector
    # Arguments
        x: numpy array/list
    # Returns
        softmax of input array
    """
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)


def main():
    window_size = 2
    corpus = ["Word2vec, which is developed by Google, is one of the famous state-of-the-art algorithm."]
    corpus_tokenized, V = tokenize(corpus)
    # find out the one-hot encoded arrays of context and center words
    for i, (x, y) in enumerate(corpus2io(corpus_tokenized, V, window_size)):
        print(i, "\n center word =", y, "\n context words =\n", x)


if __name__ == '__main__':
    main()
