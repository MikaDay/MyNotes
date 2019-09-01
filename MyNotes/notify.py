from datetime import datetime
from win10toast import ToastNotifier
from time import sleep
from sys import argv
from sys import exit
toaster = ToastNotifier()

text = ""
hour = 0
minute = 0

toast_displayed = 0

def read_input():
    global text, hour, minute
    text = argv[1]
    hour = int(argv[2])
    minute = int(argv[3])

def show_notification(text):
    toaster.show_toast("Notify ",text)

def check_time(hour, minute):
    return int(datetime.now().strftime("%H")) == hour and int(datetime.now().strftime("%M")) == minute and toast_displayed == 0

if(len(argv) != 4):
    print("Programul necesita 4 argumente ca sa porneasca")
    exit()

read_input()
print(hour, minute)
while True:
    if(check_time(hour, minute)):
        show_notification(text)
        read_input() #yes or no
    sleep(5)
