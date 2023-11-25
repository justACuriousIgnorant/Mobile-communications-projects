from math import *
class COST231Model:
    # f expressed in MHz
    # d expressed in km
    # ht and hr expressed in meters
    def __init__(self, hr=0, ht=0):
        self.hr = hr
        self.ht = ht

    def lossdB(self, f,d):
        f = f * 10 ** 6
        d = d * 10 ** 3

        x = 45.5 + 35.46*log(f)
        x -= (1.1*log(f-0.7)*self.hr)
        x += (44.9 - 6.55*log(self.ht))*(log(d))
        x -= 13.82*log(self.ht)
        x = x/1000
        return x

