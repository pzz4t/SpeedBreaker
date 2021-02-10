#this software coded with Pycharm
#this software is demo
#if module are not importing. Pls import it:)
from datetime import datetime
import time
import gps
Zaman = [10, 20, 30, 40, 50, 60]
term_memory = []#short-term memory in which variables are stored
def slowdown(input_1):
    v_max = term_memory[4 + input_1*5]
    v_sd = gps.gpsdata()
    v_speed = v_sd.fix.speed
    time.sleep(0.5)
    if v_speed > v_max :
        print("your speed is slowed down")
        v_speed -= 10
        c_pump_speed = v_speed
    else :
        print("Your speed is appropriate")
        v_pump_speed_max = v_max
def control(gps_cx,gps_cy):
    d = 0
    choosen = 0
    lent = len(term_memory)
    for i in range(0,lent//5):
        for x in range(term_memory[0+i*5],term_memory[1+i*5]+1):
            if gps_cx == x:
                for x1 in range(term_memory[2+i*5],term_memory[3+i*5]+1):
                    time.sleep(0.1)
                    if gps_cy == x1 :
                        d += 1
                        choosen = i


    if d == 1:
        slowdown(choosen)
    else:
        time.sleep(0.5)
        modul_check()
def modul_check():
    gps_c = gps.gpsdata()
    gps_cx = gps_c.fix.longitude
    gps_cy = gps_c.fix.latitude
    print(gps_c)
    if  gps_cx== 00.00 and gps_cy == 00.00 :
        print("GPS module not found")
        time.sleep(0.5)
    else:
        control(gps_cx,gps_cy)
def configuration(d):
    try:
        d = d.replace("\\","")
        d = d.replace("n","")
        d = d.replace("'","",2)
        d = int(d)

        term_memory.append(d)
    except:
        bos = 0
def arrangement():
    while True :
        time = datetime.now()
        if time.second in Zaman :
            sabit = 1

        else :
            file = open(__import__("os").environ["USERPROFILE"] + r"\Desktop\spbreaker.txt", mode="r")
            for i in range(0, 10000000):
                x = file.readline()

                if x == "":
                    file.close()
                    opening()

                    pass

                configuration(x)



def opening():
    modul_check()
    opening()
arrangement()

