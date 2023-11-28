import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from pylab import cm
import numpy as np

class PlotterClass:
    lw = 2  #linewidth
    def __init__(self, data, params):
        self.probs = data
        self.params = params

    def __truncate(self, number, digits) -> float:
        # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
        nbDecimals = len(str(number).split('.')[1])
        if nbDecimals <= digits:
            return number
        stepper = 10.0 ** digits
        return math.trunc(stepper * number) / stepper

    def generate_slider(self, label, valmin, valmax, valinit, valstep, axes_list):

        f = plt.axes(axes_list)
        slider = Slider(f, label, valmin, valmax, valinit=valinit, valstep=valstep)
        return slider


    def gen_data_sigma(self,sigmas):
        plots = []
        for sigma in sigmas:
            x = [x[0] for x in self.probs if x[1] == sigma and x[3]==self.params['f']]  # distance
            y = [x[2] for x in self.probs if x[1] == sigma and x[3]==self.params['f']]  # prob
            plots.append((x, y))
        return plots
    def gen_data_distance(self,distances):
        plots = []
        for dist in distances:
            x = [x[1] for x in self.probs if x[0] == dist and x[3]==self.params['f']]  # distance
            y = [x[2] for x in self.probs if x[0] == dist and x[3]==self.params['f']]  # prob
            plots.append((x, y))
        return plots

    #plot_sigma() effettua il print del plot con:
    # - asse x la distanza
    # - asse y la probabilit
    # - slider per il valore di sigma
    def plot_slider_sigma(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.ylim((0, 1))
        sv = 6  # define the starting value of sigma
        x = [x[0] for x in self.probs if x[1] == sv]
        y = [x[2] for x in self.probs if x[1] == sv]
        l, = plt.plot(x, y,lw=self.lw)

        slider = self.generate_slider("Sigma: ", 0,12.01,sv,0.01, [0.25, 0.2, 0.65, 0.03])

        def update(val):
            bound = self.__truncate(slider.val, 2)
            # probabilità con varianza fissa e distanza variabile
            x = [x[0] for x in self.probs if x[1] == bound]
            y = [x[2] for x in self.probs if x[1] == bound]
            l.set_xdata(x)
            l.set_ydata(y)
            print(y)

        # Call update function when slider value is changed
        slider.on_changed(update)

        # display graph
        plt.show()


    def plot_sigmas(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.xlim((1, 10))
        sv = 0.1  # define the starting value of sigma
        sigmas = [1, 3, 5, 8, 12]
        colors = ["#4D1A1A", "#B03C3C", "#D94A4A", "#C68B8A", "#FFC2B5"]
        plots_data = self.gen_data_sigma(sigmas)
        for i in range(len(sigmas)):
            ax.plot(plots_data[i][0], plots_data[i][1], label="s = "+str(sigmas[i]), color=colors[i], lw=self.lw)
        ax.legend()
        plt.xlabel("Distance (km) ")
        plt.ylabel("Probability")
        plt.title("Probability(distance)")
        # display graph
        plt.show()


    def plot_slider_distance(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.ylim((0, 1))
        sd = 5  # define the starting value of distance
        x = [x[1] for x in self.probs if x[0] == sd]
        y = [x[2] for x in self.probs if x[0] == sd]
        l, = plt.plot(x, y, lw=self.lw)

        slider = self.generate_slider('Distance (km)', 0, 10.1, sd, 0.1,[0.25, 0.2, 0.65, 0.03])

        def update(val):
            bound = self.__truncate(slider.val, 1)
            # probabilità con varianza fissa e distanza variabile
            x = [x[1] for x in self.probs if x[0] == bound]
            y = [x[2] for x in self.probs if x[0] == bound]
            l.set_xdata(x)
            l.set_ydata(y)
            print(y)

        # Call update function when slider value is changed
        slider.on_changed(update)

        # display graph
        plt.show()

    def plot_distances(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.xlim((0, 12))
        distances = [1, 3, 5, 7, 10]
        colors = ["#4D1A1A", "#B03C3C", "#D94A4A", "#C68B8A", "#FFC2B5"]
        plots_data = self.gen_data_distance(distances)
        for i in range(len(distances)):
            ax.plot(plots_data[i][0], plots_data[i][1], label="d = " + str(distances[i]), color=colors[i], lw=self.lw)
        ax.legend()
        plt.xlabel("Sigmas  ")
        plt.ylabel("Probability")
        plt.title("Probability(sigma)")
        # display graph
        plt.show()

    def plot_loss_distance(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.xlim((0,12))
        sd = 5  # define the starting value of distance
        x = [x[1] for x in self.probs if (x[0] == sd) and (x[3] == self.params['f'])]
        y = [x[2] for x in self.probs if (x[0] == sd) and (x[3] == self.params['f'])]
        l, = plt.plot(x, y, lw=self.lw)

        slider = self.generate_slider('Distance (km)', 0, 10.1, sd, 0.1,[0.25, 0.2, 0.65, 0.03])
        def update(val):
            bound = self.__truncate(slider.val, 1)
            # probabilità con varianza fissa e distanza variabile
            x = [x[1] for x in self.probs if x[0] == bound]
            y = [x[2] for x in self.probs if x[0] == bound]
            l.set_xdata(x)
            l.set_ydata(y)
            print(y)

        # Call update function when slider value is changed
        slider.on_changed(update)

        # display graph
        plt.show()


    def gen_data_freq_sigma(self, bound):
        plots = []
        for freq in [1700, 1800, 1900, 2000]:
            print(self.probs)
            x = [x[0] for x in self.probs if ((x[1] == bound) and (x[3] == freq))]  # distance
            y = [x[2] for x in self.probs if ((x[1] == bound) and (x[3] == freq))]  # prob
            plots.append((x, y))
        return plots

    def set_data_plots(self, plots_data, plots):
        for plot, data in plots, plots_data:

            plot.set_xdata(data[0])
            plot.set_ydata(data[1])

    def plot_loss_sigma(self):
        # Create a subplot
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.35)
        plt.xlim((1, 10))
        sv = 0.1  # define the starting value of sigma

        plots_data = self.gen_data_freq_sigma(sv)

        ax.plot(plots_data[0][0], plots_data[0][1],label="f=1700",color="#22092C", lw=self.lw)
        ax.plot(plots_data[1][0], plots_data[1][1],label="f=1800",color="#872341", lw=self.lw)
        ax.plot(plots_data[2][0], plots_data[2][1],label="f=1900",color="#BE3144", lw=self.lw)
        ax.plot(plots_data[3][0], plots_data[3][1],label="f=2000",color="#F05941", lw=self.lw)

        ax.legend()

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

            colmap = cm.ScalarMappable(cmap=cm.jet)
            colmap.set_array(zs)

            ax.plot_trisurf(xs, ys, zs, cmap=cm.jet, linewidth=0.1)
        plt.colorbar(colmap, ax=ax)

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

            colmap = cm.ScalarMappable(cmap=cm.jet)
            colmap.set_array(zs)

            ax.plot_trisurf(xs, ys, zs, cmap=cm.jet)
        plt.colorbar(colmap, ax=ax)

        ax.set_xlabel('Distance (km)')
        ax.set_ylabel('Sigma')
        ax.set_zlabel('Loss')

        plt.show()


    def gen_data_freq_barplot(self, bound_dv, bound_sv):
        probs = [x[2] for x in self.probs if (x[0] == bound_dv) and (x[1] == bound_sv) and (x[3] == self.params['f'])]
        return probs

    def set_data_plots_barplot(self, plots_data):
        categories = ['Probability for 1700MHz']
        bar_width = 0.2

        data = plots_data

        plt.xticks([r + bar_width * 1.5 for r in range(len(categories))],categories)  # Imposta le etichette al centro dei gruppi

        plt.bar(r, data, width=bar_width, color='#22092C')


    def bar_plot_prob(self):
        categories = ['Probability for 1700MHz', 'Probability for 1800MHz', 'Probability for 1900MHz', 'Probability for 2000MHz']

        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)
        sv = 2.0
        dv = 5.0

        bar_width = 0.2
        r = np.arange(len(categories))
        data = self.gen_data_freq_barplot(dv,sv)
        print(data)
        bar = ax.bar(r, data, width=bar_width, edgecolor='#22092C')

        plt.ylim((0, 1))
        plt.xlabel('frequencies')
        plt.ylabel('Probability')
        plt.title('Probability of link')
        plt.legend()
        sigma_slider = self.generate_slider("Sigma: ", 0.01,12.01,6, 0.01,[0.25, 0.01, 0.65, 0.03])
        distance_slider = self.generate_slider("Distance: ",1,10.1,5,0.1,[0.25, 0.05, 0.65, 0.03])

        def update(val):
            sigma_bound = self.__truncate(sigma_slider.val, 2)
            distance_bound = self.__truncate(distance_slider.val, 1)
            # probabilità con varianza fissa e distanza variabile
            data = self.gen_data_freq_barplot(distance_bound, sigma_bound)
            self.set_data_plots_barplot(data)

        # Call update function when slider value is changed
        sigma_slider.on_changed(update)
        distance_slider.on_changed(update)
        plt.show()

    def gen_data_comparison(self, f, sigma):
        probs = [(x[0],x[2]) for x in self.probs if (x[1] == sigma) and (x[3] == f)]
        return probs

    def plot_compare(self, simulation_data, n_list):
        # simulation_data[0] distance
        # simulation_data[1] prob
        # simulation_data[2] freq
        # simulation_data[3] sigma

        # Create a subplot
        fig, ax = plt.subplots(len(n_list))
        plt.subplots_adjust(bottom=0.35)
        plt.xlim((0, 12))
        #plt.ylim((0,1))
        colors = ["#4D1A1A", "#B03C3C", "#D94A4A", "#C68B8A", "#FFC2B5"]

        for i in range(0,len(n_list)):    

            f = simulation_data[i][0][2]
            sigma = simulation_data[i][0][3]
            plots_data = self.gen_data_comparison(f,sigma)

            print(simulation_data[i])
            x1 = [x[0] for x in plots_data]
            y1 = [y[1] for y in plots_data]

            x2 = [x[0] for x in simulation_data[i]]
            y2 = [y[1] for y in simulation_data[i]]


            ax[i].plot(x1,y1, label="theoretical", color=colors[0], lw=self.lw)
            ax[i].plot(x2,y2, label=f"simulated (n={n_list[i]})", color=colors[2], lw=self.lw)

            ax[i].legend()
        plt.xlabel("Distance km")
        plt.ylabel("Probability")
        plt.title("Probability(distance)")
        # display graph
        plt.show()

