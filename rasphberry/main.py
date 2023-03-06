mport RPi.GPIO as GPIO  # import gpio
import time      #import time library
import spidev
from lib_nrf24 import NRF24   #import NRF24 library

GPIO.setmode(GPIO.BCM)       # set the gpio mode

  # set the pipe address. this address shoeld be entered on the receiver alo
pipes = [[0xE0, 0xE0, 0xF1, 0xF1, 0xE0], [0xF1, 0xF1, 0xF0, 0xF0, 0xE0]]
radio = NRF24(GPIO, spidev.SpiDev())   # use the gpio pins
radio.begin(0, 25)   # start the radio and set the ce,csn pin ce= GPIO08, csn= GPIO25
radio.setPayloadSize(32)  
radio.setChannel(0x76) 
radio.setDataRate(NRF24.BR_1MBPS)    
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()
radio.openReadingPipe(1, pipes[1])
radio.printDetails()
radio.startListening()
GPIO.cleanup()
#--------------------------------------------------------------------------------------

while True: #LOOP FUNCTION
    while not radio.available(0):
        time.sleep(1/100)
    receivedMessage=[]
    while(len(receivedMessage) == 0):
        radio.read(receivedMessage, radio.getDynamicPayloadSize())
    print("--> {}".format(receivedMessage))
    print("Converting message...")
    string=""
    for n in receivedMessage:
        if(n>=32 and n<=126):
            string+=chr(n)
    print("--> {}".format(string))