# -*- coding: utf-8 -*-
import smbus
import time
import shutil

# for RPI version 1, use bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x09

#http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
def writeData(value):
    byteValue = StringToBytes(value)
    bus.write_i2c_block_data(address,0x00,byteValue) #first byte is 0=command byte.. just is.
    return -1


def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal

file = open("test.jpg", "rb")

start = 0 
while True:
    if start == 0:
        print('sending...')
        start = 1

    str = file.read(10).decode('utf-8')
    writeData(str)
    time.sleep(0.01)
    if not str:
       print('transfer finished')
       break
