import pyautogui as p
import time as t
#-----inputs---------
from_location=input("From where you want to book a ticket?")
to_location=input("Where you want to go today?")
date=input("Enter the date of travel (DD-MM-YYYY): ")
t.sleep(5)
#------automation starts-----
p.hotkey('ctrl', 't')  # Open a new tab in the browser
p.write("https://www.irctc.co.in/nget/train-search")
p.press('enter')
t.sleep(10)
p.moveTo(959, 890)
t.sleep(1)
p.leftClick()
p.moveTo(323, 507)
t.sleep(1)
p.leftClick()
# --------Enter From-----------
p.write(from_location)
t.sleep(1)
p.moveTo(263, 596)
p.leftClick()
t.sleep(1)
p.moveTo(263, 596)
t.sleep(1)
p.leftClick()
# --------Enter To-----------
p.write(to_location)
t.sleep(1)
p.moveTo(153, 626)
t.sleep(1)
p.leftClick()
t.sleep(1)
p.moveTo(263, 685)
t.sleep(1)
p.leftClick()
# --------Enter Date-----------
p.write(date)
t.sleep(1)
p.moveTo(789, 517)
t.sleep(1)
p.leftClick()
p.hotkey('ctrl', 'a')
t.sleep(1)
p.press('delete')
t.sleep(1)
p.write(date)
t.sleep(1)
#-----------Search----------
p.moveTo(224, 815)
t.sleep(1)
p.leftClick()
t.sleep(1)

# t.sleep(5)
# x,y=p.position()
# print(x,y)

# open cv  (resolution 1920x1080 , 1280x720)
# api gpt oss 20b 
# oprn cv-> gpt
# response -> chrome

