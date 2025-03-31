import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        ser.write(b'hi\n')
        time.sleep(0.5)
        #if ser.in_waiting > 0:
        #    line = ser.readline().decode('utf-8').rstrip()
        #    print(line)
        print("message sent")
        ser.close()
        time.sleep(0.5)
        ser.open()
