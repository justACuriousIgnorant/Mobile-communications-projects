import numpy as np


class Encoder:

    def __init__(self, generator):
        self.generator1, self.generator2 = generator
        len1 = len(self.generator1)
        len2 = len(self.generator2)
        degree = max(len1, len2)

        # pad the generator array if they are not the same length
        if len1 != degree:
            self.generator1.append([0 for _ in range(degree - len1)])
        elif len2 != degree:
            self.generator2.append([0 for _ in range(degree - len2)])

    def compute_output_bits(self, msg):

        msg_bits = [ord(bit) for bit in msg]
        #
        out_bits1 = map(lambda x: x % 2, np.convolve(msg_bits, self.generator1))
        out_bits2 = map(lambda x: x % 2, np.convolve(msg_bits, self.generator2))

        # return (out_bits1, out_bits2)
        return ''.join([str(b1) + str(b2) for b1, b2 in zip(out_bits1, out_bits2)])

"""
msg = '0100'
generator = ([1, 1, 1], [1, 0, 1])
enc = Encoder(generator)
out = enc.compute_output_bits(msg)
print(out)"""