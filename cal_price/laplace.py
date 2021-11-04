import numpy as np
import math

def _noise_count(e):
    beta = 1 / e
    u1 = np.random.random()
    u2 = np.random.random()
    if u1 < 0.5:
        noise = beta * np.log(2 * u2)
    else:
        noise = -beta * np.log(2 - 2 * u2)
    return noise

class Laplace_mech(object):

    def __init__(self, x, p):
        self.x = x
        self.p = p

    def _laplace_mech(self):
        epsilon = []
        acc = []
        res = []
        noise = []
        for i in range(len(self.x)):
            # 计算epsilon
            if (self.x[i] == 0):
                self.x[i] = 1
            e = math.log(0.5) / -(abs(self.x[i]) * (1-self.p))
            beta = 1 / e
            u1 = np.random.random()
            u2 = np.random.random()
            if u1 <= 0.5:
                add_noise = beta * np.log(2 * u2)
            else:
                add_noise = -beta * np.log(2 - 2 * u2)
            res.append(self.x[i] + add_noise)
            epsilon.append(e)
        return res, max(epsilon)
