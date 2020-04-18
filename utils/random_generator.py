import numpy as np

def gen_normal_distribution(length, mu, sigma):
    return np.random.normal(mu, sigma, length)

def gen_random_list(shape):
    return np.random.rand(shape)