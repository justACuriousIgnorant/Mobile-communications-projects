import math
import numpy as np
import Model
class Simulator:
    def __init__(self, parameters):
        self.parameters = parameters
        # first instantiation of the class COST231Model
        self.model = Model.COST231Model(hr = parameters['hr'], ht = parameters['ht'])

    # truncate(number,digits) is a simple function to truncate the numbers when they exceed the number of digits indicated,
    # none cares about it
    def truncate(self, number, digits) -> float:
        # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
        nbDecimals = len(str(number).split('.')[1])
        if nbDecimals <= digits:
            return number
        stepper = 10.0 ** digits
        return math.trunc(stepper * number) / stepper

    # calculate_prob(L,sigma) that calculates and return the final probability,
    # having the Loss of the Model and the value of sigma
    def calculate_prob(self, L, sigma):
        Lmax = self.__calculate_Lmax()
        print("L:", L, ", Lmax: ", Lmax)
        argument = (Lmax - L) / (math.sqrt(2) * sigma)
        prob = 0.5 * (1 + math.erf(argument))  # undefined situation when sigma=0
        return prob

    # calculate_couples(dist,sig) calculates the cartesian product between the possible distances
    # and sigmas.
    # calculate_couples require as input:
    # - a triple representing [min_val, max_val, step] for distance
    # - a triple representing [min_val, max_val, step] for sigma
    # the output is a tuple of couples like [(dist1, sig1), (dist1, sig2), ..., (dist2,sig1),(dist2,sig2),...]
    def calculate_couples(self):
        dist = self.parameters['distance_range']
        sig  = self.parameters['sigmas_range']
        freq = self.parameters['frequences']

        distances = [self.truncate(x, 1) for x in np.arange(dist[0], dist[1], dist[2])]
        sigmas = [self.truncate(x, 2) for x in np.arange(sig[0], sig[1], sig[2])]

        # I remove y=0 because when sigma=0 the formula to calculate the probability is not valid
        couples = [(x, y, z) for x in distances for y in sigmas for z in freq if y != 0]
        return couples

    # calculate_all_prob(couples) calculate the probabilities for each of the couple of the input
    # input:    a tuple of couples, where each couple has the form [dist, sigma]
    # output:   a tuple of triples, where each triple has the form [dist,sigma,prob]
    #           a tuple of triples, where each triple has the form [dist,sigma,loss]
    def calculate_all_prob(self):
        # I calculate all the possible couples (dist,sigma)
        couples = self.calculate_couples()

        probs = []
        losses = []
        # couple[0] = distanza
        # couple[1] = sigma
        # couple[2] = frequence
        for couple in couples:
            L = self.model.lossdB(couple[2], couple[0])
            probs.append([couple[0], couple[1], self.calculate_prob(L, couple[1]), couple[2]])
            losses.append([couple[0], couple[1], L, couple[2]])
        return probs, losses


    def __calculate_Lmax(self):
        return self.parameters['pt'] - self.parameters['pr']  # dB
    def generate_samples(self, sigma, f, n):

        probs = []
        lmax = self.__calculate_Lmax()
        for d in np.arange(1,10.1, 0.1):
            d = self.truncate(d,1)
            count = 0
            for x in range(0,n):
                c = np.random.normal(0,sigma)
                loss = self.model.lossdB(f, d) + c
                if loss < lmax:
                    count+=1

            probs.append((d,count / n, f, sigma))

        return probs