# -*- coding: utf-8 -*-
import smbus
import time
# for RPI version 1, use bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x60

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

while True:
    print("sending")
    writeData("test")   
    time.sleep(5)

    print('OPEN');
    writeData("OPEN-00-00")
    time.sleep(7)

    print('WIN');
    writeData("WIN-12-200")
    time.sleep(7)
