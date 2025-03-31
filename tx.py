import smbus
import time

# for RPI version 1, use bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

# slave address
address = 0x09

#http://www.raspberry-projects.com/pi/programming-in-python/i2c-programming-in-python/using-the-i2c-interface-2
def writeData(value):
    byteValue = StringToBytes(value)
    #print(byteValue)
    bus.write_i2c_block_data(address,0x00,byteValue) #first byte is 0=command byte.. just is.
    return -1

def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal

while True:
   msg = input()
   print('sending: ',msg)
   writeData(msg)
   time.sleep(0.5)
