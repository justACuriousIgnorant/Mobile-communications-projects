import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from pylab import cm
import numpy as np

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

        sigma_slider = Slider(sigma, 'Sigma', 0, 12.01, sv, 0.01)

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
        sd = 5  # define the starting value of distance
        x = [x[1] for x in self.probs if x[0] == sd]
        y = [x[2] for x in self.probs if x[0] == sd]
        l, = plt.plot(x, y)

        distance = plt.axes([0.25, 0.2, 0.65, 0.03])
        distance_slider = Slider(distance, 'Distance (km)', 0, 10.1, sd, 0.1)

        def update(val):
            bound = self.__truncate(distance_slider.val, 1)
            # probabilità con varianza fissa e distanza variabile
            x = [x[1] for x in self.probs if x[0] == bound]
            y = [x[2] for x in self.probs if x[0] == bound]
            l.set_xdata(x)
            l.set_ydata(y)
            print(y)

        # Call update function when slider value is changed
        distance_slider.on_changed(update)

        # display graph
        plt.show()


    def plot_loss_distance(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.xlim((0,12))
        sd = 5  # define the starting value of distance
        x = [x[1] for x in self.probs if x[0] == sd]
        y = [x[2] for x in self.probs if x[0] == sd]
        l, = plt.plot(x, y)

        distance = plt.axes([0.25, 0.2, 0.65, 0.03])
        distance_slider = Slider(distance, 'Distance (km)', 0, 10.1, sd, 0.1)

        def update(val):
            bound = self.__truncate(distance_slider.val, 1)
            # probabilità con varianza fissa e distanza variabile
            x = [x[1] for x in self.probs if x[0] == bound]
            y = [x[2] for x in self.probs if x[0] == bound]
            l.set_xdata(x)
            l.set_ydata(y)
            print(y)

        # Call update function when slider value is changed
        distance_slider.on_changed(update)

        # display graph
        plt.show()


    def plot_loss_sigma(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.xlim((1, 10))
        sv = 0.1  # define the starting value of sigma
        #I select sigma and

        x1 = [x[0] for x in self.probs if x[1] == sv and x[3] == 1700]    #distance
        y1 = [x[2] for x in self.probs if x[1] == sv and x[3] == 1700]    #sigma

        x2 = [x[0] for x in self.probs if x[1] == sv and x[3] == 1800]  # distance
        y2 = [x[2] for x in self.probs if x[1] == sv and x[3] == 1800]  # sigma

        x3 = [x[0] for x in self.probs if x[1] == sv and x[3] == 1900]  # distance
        y3 = [x[2] for x in self.probs if x[1] == sv and x[3] == 1900]  # sigma

        x4 = [x[0] for x in self.probs if x[1] == sv and x[3] == 2000]  # distance
        y4 = [x[2] for x in self.probs if x[1] == sv and x[3] == 2000]  # sigma

        l1, = ax.plot(x1, y1,label="f=1700",color="#22092C")
        l2, = ax.plot(x2, y2,label="f=1800",color="#872341")
        l3, = ax.plot(x3, y3,label="f=1900",color="#BE3144")
        l4, = ax.plot(x4, y4,label="f=2000",color="#F05941")

        ax.legend()

        sigma = plt.axes([0.25, 0.2, 0.65, 0.03])
        sigma_slider = Slider(sigma, 'Sigma:', 0, 12.01,  valinit=0.1, valstep=0.01)

        def update(val):
            bound = self.__truncate(sigma_slider.val, 2)
            # probabilità con varianza fissa e distanza variabile
            x1 = [x[0] for x in self.probs if x[1] == bound and x[3] == 1700]
            y1 = [x[2] for x in self.probs if x[1] == bound and x[3] == 1700]

            x2 = [x[0] for x in self.probs if x[1] == bound and x[3] == 1800]  # distance
            y2 = [x[2] for x in self.probs if x[1] == bound and x[3] == 1800]  # sigma

            x3 = [x[0] for x in self.probs if x[1] == bound and x[3] == 1900]  # distance
            y3 = [x[2] for x in self.probs if x[1] == bound and x[3] == 1900]  # sigma

            x4 = [x[0] for x in self.probs if x[1] == bound and x[3] == 2000]  # distance
            y4 = [x[2] for x in self.probs if x[1] == bound and x[3] == 2000]  # sigma

            l1.set_xdata(x1)
            l1.set_ydata(y1)
            l2.set_xdata(x2)
            l2.set_ydata(y2)
            l3.set_xdata(x3)
            l3.set_ydata(y3)
            l4.set_xdata(x4)
            l4.set_ydata(y4)
            print(y1)

        # Call update function when slider value is changed
        sigma_slider.on_changed(update)

        # display graph
        plt.show()

    def plot3D_prob(self):

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        n = 100

        # For each set of style and range settings, plot n random points in the box
        # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
        for m, zlow, zhigh in [('o', -50, -25)]:#, ('^', -30, -5)]:
            xs = [x[0] for x in self.probs]
            ys = [x[1] for x in self.probs]
            zs = [x[2] for x in self.probs]
            ax.scatter(xs, ys, zs, marker=m)

            colmap = cm.ScalarMappable(cmap=cm.hsv)
            colmap.set_array(zs)

            ax.scatter(xs, ys, zs, c=cm.hsv(np.array(zs)/max(zs)), marker=m)
        plt.colorbar(colmap)

        ax.set_xlabel('Distance (km)')
        ax.set_ylabel('Sigma')
        ax.set_zlabel('Probability')

        plt.show()

    def plot3D_loss(self):

        fig = plt.figure()
        ax = fig.add_subplot(111,projection='3d')

        # For each set of style and range settings, plot n random points in the box
        # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
        for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
            xs = [x[0] for x in self.probs]
            ys = [x[1] for x in self.probs]
            zs = [x[2] for x in self.probs]

            colmap = cm.ScalarMappable(cmap=cm.hsv)
            colmap.set_array(zs)

            ax.scatter(xs, ys, zs, c=cm.hsv(np.array(zs)/max(zs)), marker=m)
        plt.colorbar(colmap)

        ax.set_xlabel('Distance (km)')
        ax.set_ylabel('Sigma')
        ax.set_zlabel('Loss')

        plt.show()


    def bar_plot_prob(self):
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)
        sv = 0.01
        sd = 5.0
        values = [x[2] for x in self.probs if (x[0] == sd and x[1] == sv)]
        bar = ax.bar(['probability'], values, label='Probability', color='red')
        ax.set_ylabel('Probability')
        ax.set_title('Probability of link')
        plt.ylim((0, 1))
        sigma = plt.axes([0.25, 0.01, 0.65, 0.03])
        sigma_slider = Slider(sigma, 'Sigma', 0, 12.01, valinit=0.1, valstep=0.01)
        distance = plt.axes([0.25, 0.05, 0.65, 0.03])
        distance_slider = Slider(distance, 'Distance', 1, 10.1, valinit=5, valstep=0.1)
        bar[0].set_height(values[0])
        def update(val):
            sigma_bound = self.__truncate(sigma_slider.val, 2)
            distance_bound = self.__truncate(distance_slider.val, 1)
            # probabilità con varianza fissa e distanza variabile
            values = [x[2] for x in self.probs if (x[0] == distance_bound and x[1] == sigma_bound)]
            bar[0].set_height(values[0])
            ax.set_ylabel('Probability')
            ax.set_xlabel(str(values[0]*100)+"%")
            ax.set_title('Probability of link')
            print(values)

        # Call update function when slider value is changed
        sigma_slider.on_changed(update)
        distance_slider.on_changed(update)
        plt.show()
