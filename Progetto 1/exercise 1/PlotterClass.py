import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

class PlotterClass:

    def __init__(self, data):
        self.probs = data

    def __truncate(self, number, digits) -> float:
        # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
        nbDecimals = len(str(number).split('.')[1])
        if nbDecimals <= digits:
            return number
        stepper = 10.0 ** digits
        return math.trunc(stepper * number) / stepper

    def plot_sigma(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.ylim((0, 1))
        sv = 0.1  # define the starting value of sigma
        x = [x[0] for x in self.probs if x[1] == sv]
        y = [x[2] for x in self.probs if x[1] == sv]
        l, = plt.plot(x, y)

        sigma = plt.axes([0.25, 0.2, 0.65, 0.03])
        sigma_slider = Slider(sigma, 'Sigma', -1, 1, sv, 0.01)

        def update(val):
            bound = self.__truncate(sigma_slider.val, 2)
            # probabilità con varianza fissa e distanza variabile
            x = [x[0] for x in self.probs if x[1] == bound]
            y = [x[2] for x in self.probs if x[1] == bound]
            l.set_xdata(x)
            l.set_ydata(y)
            print(y)

        # Call update function when slider value is changed
        sigma_slider.on_changed(update)

        # display graph
        plt.show()

    def plot_distance(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.ylim((0, 1))
        sv = 5  # define the starting value of sigma
        x = [x[1] for x in self.probs if x[0] == sv]
        y = [x[2] for x in self.probs if x[0] == sv]
        l, = plt.plot(x, y)

        sigma = plt.axes([0.25, 0.2, 0.65, 0.03])
        sigma_slider = Slider(sigma, 'Distance (km)', 0, 10, sv, 0.1)

        def update(val):
            bound = self.__truncate(sigma_slider.val, 1)
            # probabilità con varianza fissa e distanza variabile
            x = [x[1] for x in self.probs if x[0] == bound]
            y = [x[2] for x in self.probs if x[0] == bound]
            l.set_xdata(x)
            l.set_ydata(y)
            print(y)

        # Call update function when slider value is changed
        sigma_slider.on_changed(update)

        # display graph
        plt.show()


    def plot_loss_distance(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.xlim((-1,1))
        sv = 5  # define the starting value of sigma
        x = [x[1] for x in self.probs if x[0] == sv]
        y = [x[2] for x in self.probs if x[0] == sv]
        l, = plt.plot(x, y)

        sigma = plt.axes([0.25, 0.2, 0.65, 0.03])
        sigma_slider = Slider(sigma, 'Distance (km)', 0, 10, sv, 0.1)

        def update(val):
            bound = self.__truncate(sigma_slider.val, 1)
            # probabilità con varianza fissa e distanza variabile
            x = [x[1] for x in self.probs if x[0] == bound]
            y = [x[2] for x in self.probs if x[0] == bound]
            l.set_xdata(x)
            l.set_ydata(y)
            print(y)

        # Call update function when slider value is changed
        sigma_slider.on_changed(update)

        # display graph
        plt.show()


    def plot_loss_sigma(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.xlim((0, 10))
        sv = 0.1  # define the starting value of sigma
        #I select sigma and
        x = [x[0] for x in self.probs if x[1] == sv]
        y = [x[2] for x in self.probs if x[1] == sv]
        l, = plt.plot(x, y, )

        sigma = plt.axes([0.25, 0.2, 0.65, 0.03])
        sigma_slider = Slider(sigma, 'Sigma', -1, 1,  valinit=0.1, valstep=0.01)

        def update(val):
            bound = self.__truncate(sigma_slider.val, 2)
            # probabilità con varianza fissa e distanza variabile
            x = [x[0] for x in self.probs if x[1] == bound]
            y = [x[2] for x in self.probs if x[1] == bound]
            l.set_xdata(x)
            l.set_ydata(y)
            print(y)

        # Call update function when slider value is changed
        sigma_slider.on_changed(update)

        # display graph
        plt.show()