#!/usr/bin/env python

import time
import os, sys

Updated upstream
def analog_read():
        return dev.registers['READ'].read()

import smbus
import i2c_device

bus = smbus.SMBus(1)
t0 = time.time()


print "Begin"
while True:
    elapsed = time.time() - t0
    value = analog_read()
    print "Elapsed: ", elapsed, "Value: ", value
    time.sleep(0.1)

print "Done"
