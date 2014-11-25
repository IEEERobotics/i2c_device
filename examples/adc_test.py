#!/usr/bin/env python

import time
import os, sys
import i2c_device


def analog_read():
        return dev.registers['ADDR'].read()


dev = i2c_device.I2CDevice(1,0x48
            ,config='adc_ads7830_i2c.yaml')



t0 = time.time()
print "Begin"
while True:
    elapsed = time.time() - t0
    value = analog_read()
    print "[{:8.3f}]: {:5.3f}".format(elapsed, value)
    time.sleep(0.1)
print "Done"