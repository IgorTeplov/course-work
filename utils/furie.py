import numpy as np
from math import sqrt

class Furie:

    def __init__(self, a0, ak, bk, t2, T, k_max):
        self.a0 = a0
        self.ak = ak
        self.bk = bk
        self.t2 = t2
        self.k_max = k_max
        self.T = T

    def f(self, t, once=True, from_start=False, only_pos=False):
        k_min = -self.k_max

        if from_start:
            k_min = 0

        if abs(t) < self.t2 or not once:
            v_list = []
            for k in np.arange(k_min,self.k_max+1,1):
                alfa_deg = (2*np.pi*k*t)/self.T
                if k == 0:
                    v = np.array(self.a0/2)
                else:
                    v = self.ak(k)*np.cos(alfa_deg) + self.bk(k)*np.sin(alfa_deg)
                v_list.append(v)
            if only_pos:
                tmp_sum = np.array(v_list).sum()
                if tmp_sum > 0:
                    return tmp_sum
                else:
                    return 0
            else:
                return np.array(v_list).sum()
        return 0

    def Ak(self, k):
        return np.around(sqrt(self.ak(k)**2 + self.bk(k)**2), 3)