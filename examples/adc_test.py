#!/usr/bin/env python

import time
import os, sys
import i2c_device


def analog_read():
        return dev.registers['READ'].read()

dev = i2c_device.I2CDevice(1,0x48
            ,config='adc_ads7830_i2c.yaml')
print "test"

"""
enable.write('SD', 'DIFFERENTIAL')
enable.write('CHANNEL','ONE')
enable.write('INTERNAL_REF', 'ON')
enable.write('AD_CONV', 'ON')
"""

t0 = time.time()
print "Begin"
while True:
    elapsed = time.time() - t0
    value = analog_read()
    print "Elapsed: ", elapsed, "Value: ", value
    time.sleep(0.1)
print "Done"
