import sys
import os
import random
import textwrap
import cmd
import time

from   pyfiglet   import Figlet

user_name = []


#Figlet displays the  in "big" wordart format
f = Figlet(font='slant')
print(f.renderText('SPACE GAME'))

# Adds user to list
def addUser():
    global user_name
    user_name = []
    list_length = 1
    for i in range(list_length):
        user = input('Welcome weary traveler.  What is your name? ')
        user_name.append(user)
    

# Introduction Section
def getIntro():
    mystr = ', you find yourself looking into the stars...insert rest of starting backstory. What would you like to do?'
    result = user_name[0] + mystr
    print(result)
 
 
 # Main
if __name__ == "__main__":
    addUser()
    getIntro()
     

