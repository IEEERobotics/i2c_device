#!/usr/bin/env python

import time
import os, sys
topdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(topdir)
import i2c_device

dev = i2c_device.I2CDevice(1,0x2d,config=topdir+'/sample_configs/dmcc_i2c.yaml')
print "Device: ", dev

reg = dev.registers['PowerMotor1']
print "Register: ", reg

num = 100
start = time.time()
for i in range(num):
    reg.read()
ms = (time.time() - start) *1000
print "Read {} 16-bit signed values in {:0.2f} ms, {:0.3f} ms/read".format(num,ms,ms/num)
print

testval = 1500
print "Write positive ({}) to reg: ".format(testval)
reg.write(testval)
print "Read back from reg: ", reg.read()
print
print "Write neg (-{}) to reg: ".format(testval)
reg.write(-testval)
print "Read back from reg: ", reg.read()
print
print "Write zero to reg: "
reg.write(0)
print "Read from reg: ", reg.read()
print

t0 = time.time()
while True:
  elapsed = time.time() - t0
  dev.registers['Execute'].write('Refresh')
  pos1 = dev.registers['QEI1Position'].read()
  vel1 = dev.registers['QEI1Velocity'].read()
  voltage = dev.registers['Voltage'].read()/1000.0
  print "[{:8.3f}] QEI 1 - Voltage: {}, Pos: {}, Vel: {}".format(elapsed, voltage, pos1, vel1)



