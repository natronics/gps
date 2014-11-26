# -*- coding: utf-8 -*-
import sys
import struct
import numpy as np

# Data types
SPAIN = {
    'endian':       '<',    # little endian data
    'group':        '2h',   # IQ data is signed 16 bit integer pair
    'sample-rate':  4e6,    # 4 MSPS
}


def stdin(decoder, time):
    """Read from standard in assuming the data type matches decoder. Get the
    first 'time' number of samples

    :param decoder: type of data
    :param float time:

    :returns complex numpy array of requested data:
    """

    # Turn time into samples
    samples = int(time*decoder['sample-rate'])

    # read that many samples in from stdin into array
    packdef = decoder['endian'] + decoder['group']
    array = []
    for i in xrange(samples):
        array.append(complex(*struct.unpack(packdef, sys.stdin.read(4))))

    return np.array(array)


def file(fname, decoder, time):
    """Read from a data file assuming the data type matches decoder. Get the
    first 'time' number of samples

    :param str fname: filename
    :param decoder: type of data
    :param float time:

    :returns complex numpy array of requested data:
    """

    # Turn time into samples
    samples = int(time*decoder['sample-rate'])


    # read that many samples in from stdin into array
    with open(fname, 'rb') as rawfile:
        packdef = decoder['endian'] + decoder['group']
        array = []
        for i in xrange(samples):
            array.append(complex(*struct.unpack(packdef, rawfile.read(4))))

    return np.array(array)

