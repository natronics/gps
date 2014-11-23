#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gps import data

# read in 10 milliseconds of data assuming the spain data format
init = data.stdin(data.SPAIN, 10e-3)

print "read", len(init), "samples"
