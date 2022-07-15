#######################################################
#				 ANTI KEYLOGGER TOOL				              
#		Created by R A Iha, J Ndemwa & A K Chemiron	  
#													                        
#######################################################

# For the application to run effectively, install the following depencies;
# pip install PySimpleGUI
# pip install PyFiglet
# pip install tqdm
# python AntiKeylogger.py


import json
from subprocess import check_output
import os
import io, pyfiglet
from turtle import width
import PySimpleGUI as sg
import time, sys
from tqdm import tqdm

os.system("cls")


# Create a pop-up window 
sg.theme('DarkPurple2')
layout = [[sg.Text("Do you wish to scan the system? Press OK to continue")], [sg.Button("OK"), sg.Button("Cancel")]]

window = sg.Window("Anti Keylogger Tool", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user presses Cancel or closes window & runs the program if user presses the OK button
    if event == "OK":
        break
    else:
        if event == "Cancel" or event == sg.WIN_CLOSED:
            exit()

window.close()

class Process(object):

    def __init__(self, proc_info):
        print(proc_info)
        self.pid = proc_info[1]
        self.cmd = proc_info[0]

    def name(self):
        return '%s' % self.cmd

    def procid(self):
        return '%s' % self.pid

# Create the action to be taken when a keylogger is identified
def kill_logger(key_pid):
    
    response = input("\n\nDo you want to stop this process: y/n ?")
    if (response == "y" or response == "Y"):
     os.system('taskkill /f /im ' + key_pid )
    
    #else:
    #    pass
    exit()

def get_process_list():
    process_list = []
    sub_process = str(check_output("tasklist", shell=True).decode())
    x = io.StringIO(sub_process)
    for line in x :
        line = line.split()
        if len(line) > 0:
             
             process_list.append(line)

    return process_list

if __name__ == "__main__":

    process_list = get_process_list()
    def loading():
        print (pyfiglet.figlet_format("Anti Keylogger Tool",justify="center",width=110))
        print ("Searching for KeyLoggers....")
        for i in tqdm (range (100),desc="Loading....", ascii=False, ncols=95):
            time.sleep(0.1)
        print("Scanning Completed.")
    
    loading()
    
    process_cmd = []
    process_pid = []

    for process in process_list:
        process_cmd.append(process[0])
        process_pid.append(process[1])

l1 = open("ioc.json", "r")
l1 = json.loads(l1.read())
dict1 = l1


record = 0
flag = 1

for x in process_cmd:
    for y in dict1:
        if (x.find(y['name']) > -1):
            print("KeyLogger Detected: \nThe following proccess may be a key logger: \n\n\t" + process_pid[
                record] + " ---> " + x)
            kill_logger(x)
            flag = 0
    record += 1

if (flag):
    print("\nNo Keylogger Detected")
