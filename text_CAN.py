import serial
import time

# Configuration for RS485
PORT = 'COM3'  # Replace with your serial port (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux)
BAUD_RATE = 9600

# Initialize the serial port
ser = serial.Serial(
    port=PORT,
    baudrate=BAUD_RATE,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

def write_rs485(data):
    """Send data over RS485."""
    ser.write(data.encode())  # Encode string to bytes
    ser.flush()  # Ensure all data is sent

def read_rs485():
    """Read data from RS485."""
    if ser.in_waiting > 0:
        received_data = ser.read(ser.in_waiting)
        return received_data.decode()  # Decode bytes to string
    return None

try:
    while True:
        # Write data example
        write_rs485("Hello, RS485!")
        message = bytes([0xEB, 0x90, 0x01, 0x04, 0x11, 0x0A, 0x06, 0x0C, 0x32])
        ser.write(message)
        #print("Sent: Hello, RS485!")
        
        # Read data example
        received = read_rs485()
        if received:
            print(f"Received: {received}")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    ser.close()
