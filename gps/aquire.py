# -*- coding: utf-8 -*-
import numpy as np
from gps import prn
import cmath

sats = {}
fftdata = None

def test(sample_rate, data, sv, doppler):
    """test a sample of data using a cross-correlation technique for a signal

    :param int sample_rate: how fast the data was sampled
    :param data: numpy complex array of data
    :param int SV: test satellite number
    :param float doppler: test doppler shift

    """
    global fftdata

    if sv not in sats:
        test = prn.sample(sv, sample_rate, len(data))
        sats[sv] = np.fft.fft(test)

    if fftdata is None:
        fftdata = np.fft.fft(data)

    bin_width = sample_rate / float(len(data))

    test_case = np.roll(sats[sv], int(round(doppler/bin_width)))

    convolution = np.multiply(fftdata, test_case)
    c = np.absolute(np.fft.ifft(convolution))

    return c
