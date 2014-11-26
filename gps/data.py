# -*- coding: utf-8 -*-
import struct
import numpy as np

# Data types
SPAIN = {
    'endian':       '<',    # little endian data
    'group':        '2h',   # IQ data is signed 16 bit integer pair
    'sample-rate':  4e6,    # 4 MSPS
}

def read(flike, decoder, time):
    """Read from a data file assuming the data type matches decoder. Get the
    first 'time' number of samples

    :param str flike: filename
    :param decoder: type of data
    :param float time:

    :returns complex numpy array of requested data:
    """

    # Turn time into samples
    samples = int(time*decoder['sample-rate'])

    if hasattr(flike, 'read'):
        rawfile = flike
    else:
        rawfile = open(flike, 'rb')

    packdef = decoder['endian'] + decoder['group']
    array = []
    for i in xrange(samples):
        array.append(complex(*struct.unpack(packdef, rawfile.read(4))))

    return np.array(array)
