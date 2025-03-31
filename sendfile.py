import smbus
import time

# Initialize I2C bus
bus = smbus.SMBus(1)
slave_address = 0x08  # Replace with your slave's address

def send_data(data):
    for byte in data:
        bus.write_byte(slave_address, byte)
        time.sleep(0.01)  # Small delay to ensure transmission

# Read file and send in chunks
file_path = "text.txt"
chunk_size = 32  # Max chunk size for some libraries

with open(file_path, "rb") as f:
    while chunk := f.read(chunk_size):
        send_data(chunk)
        time.sleep(0.1)  # Delay between chunks

print("File sent successfully.")
