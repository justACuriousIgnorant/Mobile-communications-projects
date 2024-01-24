from math import *
class COST231Model:
    # f is expressed in GHz
    # d is expressed in km
    # ht and hr are expressed in meters
    def __init__(self, hr=3, ht=40):
        self.hr = hr
        self.ht = ht

    # lossdB calculates the loss using the formula of COST231.
    # the output should be in dBm
    def lossdB(self, f,d):
        x = 45.5
        x = x + (35.46*log(f,10))
        x = x - ((1.1*log(f,10))-0.7)*self.hr
        x = x + (44.9 - (6.55*log(self.ht,10)))*(log(d,10))
        x = x - 13.82*log(self.ht,10)
        print("distance: ", d)
        return x