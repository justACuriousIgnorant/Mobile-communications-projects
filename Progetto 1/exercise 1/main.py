import math
import Model
import numpy as np
import PlotterClass

#parameters
hr = 3      #meters
ht = 40     #meters
pr = -96    #dBm
pt = 40     #dBm

# truncate(number,digits) is a simple function to truncate the numbers when they exceed the number of digits indicated,
# none cares about it
def truncate(number, digits) -> float:
    # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
    nbDecimals = len(str(number).split('.')[1])
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

# calculate_prob(L,sigma) that calculates and return the final probability,
# having the Loss of the Model and the value of sigma
def calculate_prob(L, sigma):
    Lmax = pt-pr #dB
    print("L:", L, ", Lmax: ", Lmax)
    argument = (Lmax - L) / (math.sqrt(2) * sigma)
    prob = 0.5 * (1 + math.erf(argument)) #undefined situation when sigma=0
    return prob

# calculate_couples(dist,sig) calculates the cartesian product between the possible distances
# and sigmas.
# calculate_couples require as input:
# - a triple representing [min_val, max_val, step] for distance
# - a triple representing [min_val, max_val, step] for sigma
# the output is a tuple of couples like [(dist1, sig1), (dist1, sig2), ..., (dist2,sig1),(dist2,sig2),...]
def calculate_couples(dist, sig):
    distances = [truncate(x,1) for x in np.arange(dist[0], dist[1], dist[2])]
    sigmas = [truncate(x,2) for x in np.arange(sig[0], sig[1], sig[2])]
    #I remove y=0 because when sigma=0 the formula to calculate the probability is not valid
    couples = [(x, y) for x in distances for y in sigmas if y!=0]
    return couples

# calculate_all_prob(couples) calculate the probabilities for each of the couple of the input
# input:    a tuple of couples, where each couple has the form [dist, sigma]
# output:   a tuple of triples, where each triple has the form [dist,sigma,prob]
#           a tuple of triples, where each triple has the form [dist,sigma,loss]
def calculate_all_prob(couples):
    probs = []
    losses = []
    for couple in couples:
        L = model.lossdB(f, couple[0])
        probs.append([couple[0],couple[1],calculate_prob(L, couple[1])])
        losses.append([couple[0], couple[1], L])
    return probs,losses


if __name__ == '__main__':
    #first instantiation of the class COST231Model
    model = Model.COST231Model(hr = hr, ht = ht)

    distance_range = [1,10.1,0.1]
    sigmas_range = [0,12.01,0.01]

    #I calculate all the possible couples (dist,sigma)
    couples = calculate_couples(distance_range, sigmas_range)
    #I calculate all the possible probabilities and losses for each couple
    probs, losses = calculate_all_prob(couples)

    # I istantiate the class PlotterClass to plot the probabilities
    plotter_prob = PlotterClass.PlotterClass(probs)
    # I istantiate the class PlotterClass to plot the losses
    plotter_loss = PlotterClass.PlotterClass(losses)

    #plotter_prob.plot_distance()
    #plotter_prob.plot_sigma()
    #plotter_loss.plot_loss_sigma()
    #plotter_loss.plot_loss_distance()
    #plotter_prob.plot3D_prob()
    #plotter_loss.plot3D_loss()
    plotter_prob.bar_plot_prob()