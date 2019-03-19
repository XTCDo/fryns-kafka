import os
import sys
import glob
import time
import RPi.GPIO as io
import logger

def measure():
    #sensorId = ["28-03049779a481", "28-03049779bfd5"]
    sensorId = glob.glob("/sys/bus/w1/devices/" + '28*')
    try:
        temperature = [-1,-1];
        i = 0;
        for sensor in range(len(sensorId)):
            tfile = open(sensorId[sensor] + "/w1_slave")
            content = tfile.read();
            tfile.close()
            temp = content.split("\n")[1].split("=")[1]
            tempfl = str(round(int(temp)/1000, 2))
            temperature[i] = tempfl;
            print("temperatuur bedraagt " + tempfl);
            i = i+1;
            time.sleep(0.5);
        #logger.log(temperature)
        return temperature;
    except KeyboardInterrupt:
        sys.exit();