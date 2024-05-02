import serial

# Initialize serial communication with Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Adjust port accordingly

try:
    while True:
        # Read the state sent by Arduino
        state = ser.readline().decode().strip()
        
        print(state)

except KeyboardInterrupt:
    ser.close()  # Close serial connection on Ctrl+C