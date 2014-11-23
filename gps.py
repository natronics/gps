#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gps import data
from gps import aquire

# read in 10 milliseconds of data assuming the spain data format
init = data.stdin(data.SPAIN, 10e-3)
print "read in", len(init), "samples"

# search for signal in sample
print aquire.test(data.SPAIN['sample-rate'], init, 1, 0.0)