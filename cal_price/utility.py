import numpy as np
import scipy.stats
from scipy.stats import wasserstein_distance


def _softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)


class Utility(object):
    def __init__(self, h1, h2):
        self.h1 = h1
        self.h2 = h2

    def _cal_f_divergence(self):
        p = np.asarray(self.h1)
        q = np.array(self.h2)
        # 调用scipy包求解
        f = scipy.stats.entropy(p, q)
        return f

    def _cal_hellinger(self):
        p = np.asarray(self.h1)
        q = np.array(self.h2)
        h = 1/np.sqrt(2)*np.linalg.norm(np.sqrt(p)-np.sqrt(q))
        return h

    def _cal_bhattacharyya(self):
        p = np.asarray(self.h1)
        q = np.array(self.h2)
        bc = np.sum(np.sqrt(p * q))
        b = -np.log(bc)
        return b

    def _cal_cross_entropy(self):
        p = np.asarray(self.h1)
        q = np.array(self.h2)
        ce = -np.sum(q * np.log(_softmax(p)))
        return ce

    def _cal_wasserstein(self):
        return wasserstein_distance(self.h1, self.h2)
