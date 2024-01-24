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

    # Flip a bit with probability p
    def __flip__(self, bit, p=0.5):
        choices = [0, 1]
        weights = [1 - p, p]
        n = random.choices(choices, weights)[0]
        if(n==0):
            return bit
        else:
            return 1-bit


    # Send a message with crossover_probability p
    def send_message(self, message, encoder):
        # Compute the encoded message
        msg = encoder.compute_output_bits(message)
        # Flip each bit with probability p
        self.message = []
        for m in msg:
            self.message.append(int(self.__flip__(int(m), self.p)))
        return msg, self.message

    # Decode the received message using the 'viterbi' library
    def receive_message(self, constr, pol):
        vit = viterbi.Viterbi(constr, pol)

        msg = vit.decode(self.message)
        self.message = []
        return msg
