import time
import smbus
from Adafruit_LED_Backpack import Matrix8x8


I2C_address = 0x71;
I2C_bus_number = 1;
bus = smbus.SMBus(I2C_bus_number);

display = Matrix8x8.Matrix8x8() #addresses the LED Driver
bus.write_byte(I2C_address,2)
display.begin() #Initialize the Display
display.clear() #clears the display

while True:
    
    for xled in range (0,8): #starts at row 0 and goes to row 8 
        x = int((xled))
        for i in range (1,9): # Cycles through row of x 
            y = (i-1)
            display.clear()
            display.set_pixel(x,y,1) #display the LED in position
            print "position ", xled, y #prints current position
            display.write_display()
            time.sleep(.2) #sets delay of LED
                    