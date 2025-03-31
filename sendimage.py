import serial
from xmodem import XMODEM
from time import sleep

s = serial.Serial(port='/dev/ttyS0', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)

def getc(size, timeout=1):
    return s.read(size)
def putc(data, timeout=1):
    s.write(data)

modem = XMODEM(getc, putc)

f = open('test.txt', 'rb')

#s.write(b'starting file transfer\n')
stream = f.readlines()
status = modem.send(stream, retry=1)
stream.close()
#s.write(b'file transfer finished\n')
s.close()
