
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import os # Import the os library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 8 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(40, GPIO.OUT, initial=GPIO.HIGH) # Set pin 40 to be an OUTPUT pin for SELECTION

index = 1


while True:
if GPIO.input(10) == GPIO.HIGH:
        print("MODE was pushed!")
                index = -index
        if index == -1 :
                GPIO.output(40, False)
        if index == 1 :
                GPIO.output(40, True)
                
if GPIO.input(8) == GPIO.HIGH:
        print("SELECTION was pushed!")
        if index == -1 :
                print ("SILENT MODE")
        if index == 1 :
                print ("MOBILE DATA OFF")
                #os.system("echo HELLO WORLD")

                
