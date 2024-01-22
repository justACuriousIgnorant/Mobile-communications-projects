from random import random


class Channel():
    message = ""
    def __init__(self, p=0.5):
        p=1
    #set the crossover probability of the channel
    def set_crossprob(self, p=0.5):
    def __flip__(self, bit, p=0.5):
        scelte = [0, 1]
        peso = [1 - p, p]

        n = random.choices(scelte, peso)[0]

        if(n==0):
            return 1 if bit==1 else 0
        else:
            return 0 if bit==1 else 1


    #send a message with crossover_probability p
    def send_message(self, message):
        #apply random replace (__flip__)
    def receive_message(self):
        #apply viterbi