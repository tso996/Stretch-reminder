# make a pop up window
# make the timer
# import os

# body_str="It's been a while. Get up and stretch a little!"

# title_str="stretch reminder"


# os.system('Tell application "System Events" to display dialog "'+body_str+'" with title "'+title_str+'"')

import easygui
import time;
from threading import Thread


start = time.time()
status = False

def threaded_function(arg):
    for i in range(arg):
        print("running")
        easygui.msgbox("It's been a while. Get up and excercise for a bit!", title="Stretch reminder")
       
        time.sleep(1)



easygui.msgbox("It's been a while. Get up and excercise for a bit!", title="Stretch reminder")
start = time.time()

if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (10, ))
    while True:
     if time.time() - start > 5:
        start = time.time()
        thread.start()
        thread.join()
    print("thread finished...exiting")