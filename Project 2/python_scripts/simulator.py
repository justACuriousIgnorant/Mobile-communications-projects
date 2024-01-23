import random
from viterbi import Viterbi
import numpy as np
import Channel
import Encoder
import PlotterClass

"""
messages_generator() creates a number of samples with a specific length
@:param nsamples define the number of samples to be generated
@:param len define the length of the messages generated 
@:return the list of final samples
"""
def messages_generator(nsamples, len) -> list:
    messages = []
    for x in range(nsamples):
        m = ""
        for c in range(len):

            m+=str(random.choices([0,1])[0])
        messages.append(m)
    return messages

"""
calc_BERs() calculate the value of BER for each generator specified
"""
def calc_BERs(n_samples, msg_len, genA, genB, step,stop ):


    messages = messages_generator(n_samples, msg_len)
    probs = np.arange(0, stop + step, step)

    channel = Channel.Channel()

    enc_A = Encoder.Encoder(genA)
    enc_B = Encoder.Encoder(genB)

    BER_A = []
    BER_B = []
    for id, p in enumerate(probs):
        BER_A_temp = 0
        BER_B_temp = 0
        print("COMPLETED...: ",(id/len(np.arange(0,stop+step,step)))*100, "%")
        for id, m in enumerate(messages):
            channel.set_crossprob(p)

            msg_enc_A, msg_sent_A = channel.send_message(m, enc_A)
            rcv_msg_A = channel.receive_message(3, [0o4, 0o5])


            msg_enc_B, msg_sent_B = channel.send_message(m, enc_B)
            rcv_msg_B = channel.receive_message(3, [0o7, 0o5])

            BER_A_temp += (sum(x != y for x, y in zip([int(x) for x in m], rcv_msg_A[:msg_len])) / len(msg_enc_A))
            BER_B_temp += (sum(x != y for x, y in zip([int(x) for x in m], rcv_msg_B[:msg_len])) / len(msg_enc_B))

        BER_A.append((p, BER_A_temp / n_samples))
        BER_B.append((p, BER_B_temp / n_samples))
    print("END!")
    return BER_A, BER_B

if __name__ == '__main__':
    n_samples = 10000
    msg_len = 30
    step = 0.005
    stop = 0.20
    generator_A = ([1, 0, 0], [1, 0, 1])
    generator_B = ([1, 1, 1], [1, 0, 1])

    BER_A, BER_B = calc_BERs(n_samples, msg_len, generator_A, generator_B, step, stop)

    plotter = PlotterClass.PlotterClass([BER_A, BER_B])
    plotter.plot_probs()