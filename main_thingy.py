from adminblocks import *
from userblocks import *
import pyinputplus as pyip
mainmode = pyip.inputInt(prompt="Type '1' for admin mode, '2' for user mode and '3' to exit.",min=1,max=3)
if mainmode == 1:
    if adminCheck():
        Data_Choice()
elif mainmode == 2:
    User_Intro()
            