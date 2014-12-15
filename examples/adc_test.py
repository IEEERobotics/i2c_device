#!/usr/bin/env python

import time
import os, sys


import smbus
import i2c_device

dev = i2c_device.I2CDevice(1,0x48,config='adc_ads7830_i2c.yaml')

t0 = time.time()
print "Registers: ", dev.registers
print "Command: ", dev.command
print "Begin"
while True:
    elapsed = time.time() - t0
    value = dev.registers['CH1'].read()
    print "Elapsed: ", elapsed, "Value: ", value
    time.sleep(0.1)

print "Done"
