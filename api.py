import pandas as pd
import numpy as np


def add_explanation(front,  back):
    """
    index 0 is uniq id, 1 is front, 2 is back, 3 is explanation, 4 is tags
    """
    random_words = ["example", "sample", "test", "demo"]
    return np.random.choice(random_words)
