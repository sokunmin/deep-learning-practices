"""
Tutorial video: https://www.youtube.com/watch?v=bqeUmLCgsVw

"""

import glob
import sys
from random import shuffle

import cv2
import tensorflow as tf


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value[value]))


def load_image(addr):
    # read an image and resize to (224, 224)
    # cv2 load dogs_and_cats as BGR, convert it to RGB
    img = cv2.imread(addr)
    if img is None:
        return None

    img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def create_data_record(output_filename, addrs, labels):
    # open the TFRecords file
    writer = tf.python_io.TFRecordWriter(output_filename)
    for i in range(len(addrs)):
        # print how many dogs_and_cats are saved every 1000 dogs_and_cats
        if not i % 1000:
            print('Train data: {}/{}'.format(i, len(addrs)))
            sys.stdout.flush()
        # Load the image
        img = load_image(addrs[i])

        label = labels[i]

        if img is None:
            continue

        # Create a new feature
        feature = {
            'image_raw': _bytes_feature(img.tostring()),
            'label': _int64_feature(label)
        }

        # Create an example protocol buffer
        example = tf.train.Example(features=tf.train.Features(feature=feature))

        # Serialize to string and write on the file
        writer.write(example.SerializeToString())

    writer.close()
    print('Writing {} is done'.format(output_filename))
    sys.stdout.flush()


def create_dataset():
    cat_dog_train_path = 'data/dogs_and_cats/*/*.jpg'
    # read addresses and labels from the `train` folder
    addrs = glob.glob(cat_dog_train_path)
    # 0 = Cat, 1 = Dog
    labels = [0 if 'cat' in addr else 1 for addr in addrs]

    # [1] to shuffle data
    c = list(zip(addrs, labels))
    shuffle(c)
    addrs, labels = zip(*c)
    # [2] shuffle indices by permutation
    # TODO:

    # Divide the data into 60% train, 20% validation, and 20% test
    train_ratio = 0.6 * len(addrs)
    val_ratio = 0.8 * len(addrs)

    train_addrs = addrs[0:train_ratio]
    train_labels = labels[0:train_ratio]

    val_addrs = addrs[train_ratio: val_ratio]
    val_labels = labels[train_ratio: val_ratio]

    test_addrs = addrs[val_ratio:]
    test_labels = labels[val_ratio:]

    create_data_record('train.tfrecords', train_addrs, train_labels)
    create_data_record('val.tfrecords', val_addrs, val_labels)
    create_data_record('test.tfrecords', test_addrs, test_labels)


if __name__ == '__main__':
    create_dataset()