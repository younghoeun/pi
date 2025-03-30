import time
import pigpio

SDA=18
SCL=19

I2C_ADDR=9

def i2c(id, tick):
   global pi
   global status
   # s: tuple of the status
   # b: number of bytes,
   # d: bytearray containing the read bytes
   s, b, d = pi.bsc_i2c(I2C_ADDR)
   print(status)

   if b:
      print(d)
      status = 0
      if d == b'\x00finished':
         print('file transfer finished')
         status = 1
      f.write(d.decode('utf-8'))


pi = pigpio.pi()

if not pi.connected:
    exit()

# Add pull-ups in case external pull-ups haven't been added

pi.set_pull_up_down(SDA, pigpio.PUD_UP)
pi.set_pull_up_down(SCL, pigpio.PUD_UP)

# Respond to BSC slave activity

status = 0

filename = input("file name: ")
f = open(filename,"w")
f = open(filename,"a")

e = pi.event_callback(pigpio.EVENT_BSC, i2c)

pi.bsc_i2c(I2C_ADDR) # Configure BSC as I2C slave

while status == 0:
   time.sleep(0.1)

e.cancel()

pi.bsc_i2c(0) # Disable BSC peripheral

pi.stop()

f.close
