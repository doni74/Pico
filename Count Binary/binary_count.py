from machine import Pin
from time import sleep

# Define the GPIO pins for LEDs
led_pins = [Pin(pin_num, Pin.OUT) for pin_num in [10, 12, 13, 15]]

def count_binary():
    for i in range(16):  # Count from 0 to 15 in binary
        binary_value = bin(i)[2:]  # Convert to binary
        binary_value = '0' * (4 - len(binary_value)) + binary_value  # Pad with zeros to ensure 4 digits
        for j, bit in enumerate(reversed(binary_value)):
            led_pins[j].value(int(bit))  # Set the LED pin to the corresponding binary value
        sleep(1)  # Pause for 1 second between each count

# Call the function to start counting in binary
while True:
    count_binary()
    sleep(1)
