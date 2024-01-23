import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from pylab import cm
import numpy as np

class PlotterClass:
    lw = 1 #linewidth
    def __init__(self, data):
        self.data = data
        self.probs = [[d[0] for d in data[0]], [d[0] for d in data[1]]]
        self.BERs = [[d[1] for d in data[0]], [d[1] for d in data[1]]]

    def plot_probs(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.grid(True, which='both', linestyle='--', alpha=0.3)

        colors = ["#4D1A1A", "#D94A4A"]
        probs = self.probs
        bers = self.BERs
        prob_highlight = [0.01, 0.020, 0.05, 0.1, 0.15,0.20]
        ber_highlight_A = [x[1] for x in self.data[0] if x[0] in prob_highlight]
        ber_highlight_B = [x[1] for x in self.data[1] if x[0] in prob_highlight]

        ax.plot(probs[0], bers[0], label="gen = (1, 1+D²)", color=colors[0], lw=self.lw)
        ax.plot(probs[1], bers[1], label="gen = (1+D+D², 1+D²)" , color=colors[1], lw=self.lw)

        ax.scatter(prob_highlight, ber_highlight_A, color=colors[0], lw=self.lw, s=20, marker='+')
        ax.scatter(prob_highlight, ber_highlight_A, color=colors[0], lw=self.lw, s=20, marker='x')

        ax.scatter(prob_highlight, ber_highlight_B, color=colors[1], lw=self.lw, s=20, marker='+')
        ax.scatter(prob_highlight, ber_highlight_B, color=colors[1], lw=self.lw, s=20, marker='x')

        # Linee tratteggiate verso l'asse x
        for i in range(len(prob_highlight)):
            plt.hlines(ber_highlight_A[i], 0, prob_highlight[i], linestyle='dashed', color=colors[0], linewidth=1)

        for i in range(len(prob_highlight)):
            plt.hlines(ber_highlight_B[i], 0, prob_highlight[i], linestyle='dashed', color=colors[1], linewidth=1)


        # Linee tratteggiate verso l'asse y
        for i in range(len(prob_highlight)):
            plt.vlines(prob_highlight[i], 0, ber_highlight_A[i], linestyle='dashed', color=colors[0], linewidth=1)

        # Linee tratteggiate verso l'asse y
        for i in range(len(prob_highlight)):
            plt.vlines(prob_highlight[i], 0, ber_highlight_B[i], linestyle='dashed', color=colors[1], linewidth=1)

        plt.xticks(np.arange(0,0.21, 0.01))

        plt.yscale('log')
        ax.legend(loc='lower right')
        plt.xlabel("Probability")
        plt.ylabel("Bit Error Rate")
        plt.title("BER(p)")
        # display graph
        plt.show()


