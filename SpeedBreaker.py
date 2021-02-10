#this software coded with Pycharm
#if module are not importing. Pls import it:)
from datetime import datetime
import time
Zaman = [10,20,30,40,50,60]
a_constant = 1 #constant
time_ = datetime.now()#current time
lıst_0 = []#short-term memory in which variables are stored
def Opening():#opening menu
    print("""
Welcome to the zone adding interface""")
    time.sleep(1)
    print("""
Type (A) to add a zone.
Type (E) to exit the program.""")
    bas_yon = input("")
    if bas_yon == "a":
        Positioning()
    elif bas_yon == "B":
        Positioning()
    elif bas_yon == "E":
        exit(0)
    elif bas_yon == "e":
        exit(0)
    else :
        print("""
Please choose one of the selected options.
You are taken back to the main menu.""")
        time.sleep(1)
        Opening()
def Positioning():#input menu
    try :
        start_x = input("The starting X coordinate of the region you want to add =")
        end_x = input("The Ending X coordinate of the region you want to add =")
        start_y = input("The starting Y coordinate of the region you want to add =")
        end_y = input("The ending Y coordinate of the region you want to add =")
        limit_speed = input("Max speed = ")
        x_start,x_end,y_start,y_end,sp_max = int(start_x),int(end_x),int(start_y),int(end_y),int(limit_speed)

    except  ValueError :
        print("""
Please make sure the numbers entered are integers...""")
        Positioning()
    else :
        print("""
Saving procces is started ...
Please do not close the program until the save process is finished.""")
        lıst_0.append(sp_max)#i added the variables reverse because under this code ı erasing the variables inversely
        lıst_0.append(y_end)
        lıst_0.append(y_start)
        lıst_0.append(x_end)
        lıst_0.append(x_start)
        print(lıst_0)
        saving()
def saving() :#save menu
    while True:
        time_ = datetime.now()
        if time_.second in Zaman: # Timed recording so there are no problems with the file
            file = open(__import__("os").environ["USERPROFILE"] + r"\Desktop\spbreaker.txt", mode="a")#this is a demo so ı use txt file as a server
            for i in range(4,-1,-1): #reverse loop
                loop_ı = str(lıst_0.pop(i))
                file.write(loop_ı + "\n")

            file.close()
            print("the file has been saved...")
            print("""
You send it back to the main menu.""")
            time.sleep(1)
            Opening()
Opening()

