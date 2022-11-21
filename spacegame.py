import sys
from   pyfiglet   import Figlet

#Figlet displays the  in "big" wordart format
f = Figlet(font='doom')
print(f.renderText('SPACE GAME'))

print(" Welcome explorer.  What is your name?")

# Introduction Section
def getIntro():
    print("You find yourself looking into the stars...")
 

#Login Section.  Requires the user to login (case sensative). 
user_list = ["Elliot", "Chris", "Brandon"]
user_name = input()
while user_name in user_list:
    print(f"Welcome " + user_name)
    getIntro()
    break
else:
    print("Unauthorized user.  Please enter valid username: ")
    quit()            
    

    
