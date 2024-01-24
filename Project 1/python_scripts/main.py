import math
import Model
import numpy as np
import PlotterClass
import Simulator

parameters={
    'hr':3,     #meters
    'ht':40,    #meters
    'pr':-96,   #dBm
    'pt':56,     #dBm
    'distance_range': [1, 10.1, 0.1],       #km
    'sigmas_range': [0, 12.01, 0.1],
    'frequences': [1700, 1800, 1900, 2000],  #MHz
    'f':1700,

}



if __name__ == '__main__':
    simulator = Simulator.Simulator(parameters)

    #I calculate all the possible probabilities and losses for each couple
    probs, losses = simulator.calculate_all_prob()

    # I istantiate the class PlotterClass to plot the probabilities
    plotter_prob = PlotterClass.PlotterClass(probs, parameters)
    # I istantiate the class PlotterClass to plot the losses
    #plotter_loss = PlotterClass.PlotterClass(losses, parameters)

    #plotter_prob.plot_distance()
    #plotter_prob.plot_sigma()
    #plotter_loss.plot_loss_sigma()
    #plotter_loss.plot_loss_distance()
    #plotter_prob.plot3D_prob()
    #plotter_loss.plot3D_loss()
    #plotter_prob.bar_plot_prob()
    plotter_prob.plot_sigmas()
    plotter_prob.plot_distances()


    ##Simulation approach
    results=[]
    sigma = 5
    f = 1700
    results.append(simulator.generate_samples(sigma, f, 50))
    results.append(simulator.generate_samples(sigma, f, 5000))
    plotter_prob.plot_compare(results, [50,5000])
