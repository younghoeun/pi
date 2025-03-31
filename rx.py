import time
import pigpio
import subprocess
import os
import sys

# GPIO setting
SDA=18
SCL=19

# Slave address
I2C_ADDR=9

def readfile(filename):
   try:
      f = open(filename,'r')
      print(f.read())
   except:
      print("no file name ", filename)

def i2c(id, tick):
   global pi
   global status
   # s: tuple of the status
   # b: number of bytes,
   # d: bytearray containing the read bytes
   s, b, d = pi.bsc_i2c(I2C_ADDR)
   sys.stdout = sys.__stdout__

   if b:
      header = d[0:4]
      #print(d)
      if header == b'\x00run':
         cmd = d[5:]
         filename = 'output.log'
         with open(filename,'w') as f:
            sys.stdout = f
            output = subprocess.getoutput(cmd.decode('utf-8'))
            print(output)
            sys.stdout = sys.__stdout__
         print("command executed")
         readfile(filename)
         os.system("sshpass -p qwe123 scp output.log pi@192.168.50.101:/home/pi/output.log")

      if d == b'\x00show':
         readfile('output.log')

      if d == b'\x00exit':
         status = 0

pi = pigpio.pi()

if not pi.connected:
    exit()

# Add pull-ups in case external pull-ups haven't been added
pi.set_pull_up_down(SDA, pigpio.PUD_UP)
pi.set_pull_up_down(SCL, pigpio.PUD_UP)

# Respond to BSC slave activity
e = pi.event_callback(pigpio.EVENT_BSC, i2c)

pi.bsc_i2c(I2C_ADDR) # Configure BSC as I2C slave

status = 1
while status:
   time.sleep(0.1)

e.cancel()

pi.bsc_i2c(0) # Disable BSC peripheral

pi.stop()

