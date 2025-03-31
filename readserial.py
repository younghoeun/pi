import serial
import time

if __name__ == '__main__':
    ser = serial.Serial('/dev/serial0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        time.sleep(0.5)

