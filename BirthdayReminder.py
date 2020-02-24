import time
from win10toast import ToastNotifier
birthdayFile = 'D:/Python Script for Reminder/Birthdaydata.txt'

def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')    
    today = time.strftime('%m%d')    
    flag = 0
    toaster=ToastNotifier()
    for line in fileName:
        if today in line:
            line = line.split(' ')            
            firstname = line[1]           
            secondname = line[2]            
            flag = 1
            # line[1] contains Name and line[2] contains Surname
            #toaster=ToastNotifier()
            toaster.show_toast("Birthdays Today !", firstname + ' ' + secondname, duration=10)            
    if flag == 0:
    	    toaster.show_toast("Birthdays Today !", "No Birthdays Today", duration=10)
        

if __name__ == '__main__':
    checkTodaysBirthdays()