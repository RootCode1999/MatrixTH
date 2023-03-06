from sys import flags
import time
from threading import Thread
import os
from writetemhum import writetemhum

class NewThread(Thread):
    flag = 0
    def __init__(self):
        Thread.__init__(self) 
    def run(self):
        while(True):  
            time.sleep(10)
            # os.system("/home/pi/matrixth/back_end/get.sh")
            writetemhum()
            print("--------------------------------------")

