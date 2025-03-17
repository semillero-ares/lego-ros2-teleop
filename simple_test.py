#!/usr/bin/env python3
"""Simple script to test Bluetooth serial connection"""

import serial
import serial.tools.list_ports

# First: Show all available serial ports
print("Looking for serial ports...")
ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Found: {port.device} - {port.description}")

# Second: Try to connect to a specific port
try:
    # Replace X with your COM port number minus 1 (e.g., for COM3, use ttyS2)
    PORT = "/dev/ttyS2"
    
    print(f"\nTrying to connect to {PORT}...")
    ser = serial.Serial(PORT, baudrate=9600, timeout=1)
    
    print("Success! Connection is open.")
    print("Press Ctrl+C to exit")
    
    while True:
        pass  # Just keep the connection open
        
except KeyboardInterrupt:
    print("\nTest ended by user")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Always close the port if it was opened
    if 'ser' in locals():
        ser.close()
        print("Port closed") 