import pyautogui
import time
from time import sleep
import sys


class Cordinates:
    def wr_cor(self):
        pyautogui.click(self.corx, self.cory)
cor = Cordinates()
cor.corx = 1243 
cor.cory = 647

cor.wr_cor()

print("The spam bot will paste and enter to wherever your mouse has clicked.")
print("To trigger a failsafe that stops the bot, position your mouse at a corner of the screen")
string = input("What do you want to spam?")
spamfilter = input("What should be the interval at which the program spams? (In seconds) ")
maxcount = int(input("How many times do you want to spam?")) - 1

print("IT WILL START SPAMMING IN 5 SECONDS")
count = 0
sleep(3)
while count <= maxcount:
        pyautogui.write(string)
        pyautogui.press('enter', interval=spamfilter)
        count += 1
sys.exit()
