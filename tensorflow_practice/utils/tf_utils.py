from __future__ import division, print_function, unicode_literals

import tensorflow as tf
import numpy as np
import os


def reset_graph(seed=42):
    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.seed(seed)


import matplotlib
import matplotlib.pyplot as plt

# To plot pretty figures
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

# Where to save the figures
PROJECT_ROT_DIR = "."
CHAPTER_ID = 'tensorflow'


def save_fig(fig_id, tight_layout=True):
    path = os.path.join(PROJECT_ROT_DIR, 'dogs_and_cats', 'CHAPTER_ID', fig_id + ".png")
    print('Saving figure', fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format='png', dpi=300)
