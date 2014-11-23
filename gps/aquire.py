# -*- coding: utf-8 -*-
import numpy as np
from gps import prn

# pre-compute PRN at sample rate
SV = {i: prn.PRN(i) for i in range(1, 33)}


def test(sample_rate, data, sv, doppler):
    """test a sample of data using a cross-correlation technique for a signal

    :param int sample_rate: how fast the data was sampled
    :param data: numpy complex array of data
    :param int SV: test satellite number
    :param float doppler: test doppler shift

    """

    # zero doppler
    base_frequency = 1.023e6
    f = base_frequency + doppler

    sat = [-1 if x==0 else x for x in SV[sv]]
    test_case = []
    for i in range(len(data)):
        t = i * sample_rate**-1
        test_case.append(sat[int(t*f)%1023])
    test_case = np.array(test_case)

    return np.correlate(test_case, data, 'full')
