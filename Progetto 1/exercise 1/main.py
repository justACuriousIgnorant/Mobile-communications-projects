import math
import Model
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import PlotterClass
hr = 3 #meters
ht = 40 #meters
f = 1700 #MHz
d = 10 #km
pr = -90 #dBm
pt = 40 #dBm

def truncate(number, digits) -> float:
    # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
    nbDecimals = len(str(number).split('.')[1])
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def calculate_prob(L, sigma):

    Lmax = pt / pr
    print("L:", L, ", Lmax: ", Lmax)
    prob = 0.5 * (1 + math.erf((Lmax - L) / (math.sqrt(2) * sigma)))
    #print(prob)
    return prob

def calculate_couples(dist, sig):
    distances = [truncate(x,1) for x in np.arange(dist[0], dist[1], dist[2])]
    sigmas = [truncate(x,2) for x in np.arange(sig[0], sig[1], sig[2])]
    couples = [(x, y) for x in distances for y in sigmas if y!=0]
    print(couples)
    return couples

def calculate_all_prob(couples):
    probs = []
    for couple in couples:
        L = model.lossdB(f, couple[0])
        probs.append([couple[0],couple[1],calculate_prob(L, couple[1])])

    return probs
def calculate_all_loss(couples):
    losses = []
    for couple in couples:
        L = model.lossdB(f, couple[0])
        losses.append([couple[0], couple[1], L])
    return losses

import sys

if __name__ == '__main__':
    model = Model.COST231Model(hr = hr, ht = ht)
    distance_range = [0.1,10.1,0.1]
    sigmas_range = [-1,1.01,0.01]

    couples = calculate_couples(distance_range, sigmas_range)
    probs = calculate_all_prob(couples)

    plotter_prob = PlotterClass.PlotterClass(probs)
    plotter_prob.plot_distance()
    plotter_prob.plot_sigma()

    losses = calculate_all_loss(couples)
    plotter_loss = PlotterClass.PlotterClass(losses)
    plotter_loss.plot_loss_sigma()
    plotter_loss.plot_loss_distance()


