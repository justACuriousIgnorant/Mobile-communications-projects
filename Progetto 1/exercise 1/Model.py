from math import *
class COST231Model:
    # f expressed in GHz
    # d expressed in km
    # ht and hr expressed in meters
    def __init__(self, hr=0, ht=0):
        self.hr = hr
        self.ht = ht

    def lossdB(self, f,d):
        f = f * 10 ** 6
        d = d * 10 ** 3

        x = 45.5 + 35.46*log(f,10)
        x -= (1.1*log(f,10)-0.7)*self.hr
        x += (44.9 - 6.55*log(self.ht,10))*(log(d,10))
        x -= 13.82*log(self.ht,10)
        x = x/1000
        return x