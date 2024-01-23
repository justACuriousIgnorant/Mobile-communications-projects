import random
import viterbi as viterbi
import Encoder
class Channel():

    def __init__(self, p=0.5):
        self.p=p
        self.message = []
    #set the crossover probability of the channel
    def set_crossprob(self, p):
        self.p = p
    def __flip__(self, bit, p=0.5):
        scelte = [0, 1]
        peso = [1 - p, p]

        n = random.choices(scelte, peso)[0]

        if(n==0):
            return 1 if bit==1 else 0
        else:
            return 0 if bit==1 else 1


    #send a message with crossover_probability p
    def send_message(self, message, encoder):
        msg = encoder.compute_output_bits(message)
        self.message = []
        for m in msg:
            self.message.append(int(self.__flip__(int(m), self.p)))
        return msg, self.message

    def receive_message(self, constr, pol):
        vit = viterbi.Viterbi(constr, pol)

        msg = vit.decode(self.message)
        self.message = []
        return msg
