import sys
import time

a = 0.4
b = 0.2
c = 0.08

credits = 0
age = 20
fuel = 0


## game paths and loops ##

def intro():
    print()
    print("(## DEEP SPACE III but in text! ###)")
    time.sleep(a)
    print("You look around you, seemingly nothing but barren wastes....but wait")
    time.sleep(a)
    print("you see something, a cave....")
    time.sleep(a)
    print("you head inside, as there is nothing else for miles....")
    time.sleep(a)
    print("The ground starts rumbling...")
    time.sleep(a)
    print("Your helmet light cuts through the darkness...")
    time.sleep(a)
    print()
    question = '"I Have a bad feeling about this.. (you think to yourself)"'
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(b)
    print()
    print()
    print("As you venture inside you see the cave splits off into several tunnels....")
    time.sleep(a)
    print("Three paths are revealed:")
    time.sleep(a)
    print()
    print("Path #1: Go down the Left path, *you see what looks to be claw marks on the walls*....")
    time.sleep(a)
    print("Path #2: Go down the Center path, *you think to yourself you heard faint humming coming from this direction*....")
    time.sleep(a)
    print("Path #3: Go down the right path *you sense it's warmer down this path, and yet your body goes cold when you look at it*...")
    time.sleep(a)
    print()
    firstPath = input("Which path will you choose? (1/2/3): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()
    elif firstPath == '3':
        print()
        path3()

def path1():
    print("As you go down the path you begin to see dried blood and old bones, human bones....")
    time.sleep(a)
    print("you can tell this tragedy happened a while ago, so you calm yourself and explore the room..")
    time.sleep(a)
    print("After the grizzly job of searching the bodies, you've collected 5000 Credits..maybe you'll find some use for these later....")
    time.sleep(a)
    print("nothing of value remains, you head back to where the cave splits....")
    time.sleep(a)
    print("you find the other paths are no longer there, the stone seemingly smoothed over, only the exit remains....")
    time.sleep(a)
    print("As you exit the cave your scanner starts beeping....")
    time.sleep(a)
    #some how in this path we need to add credits to the varriable posted at the top of the code
    


def path2():
    print("you walk the path until you come into a large room")
    time.sleep(a)
    print("")
    time.sleep(a)


def path3():
    print("You walk down the path, you see a bright green glow that seems just around the bend, but you can't quite catch it...")
    time.sleep(a)
    print("You feel Darkness suddenly begin to envolpe you, your head swirls and you feel like the world itself is spinning around you....")
    time.sleep(a)
    print("As you feel your eyes close for what you know is the last time, you see the display on your arm blaring a warning...")
    time.sleep(a)
    print("## INTENSE GAMMA RADIATION BURST DETECTED ###..")
    time.sleep(a)
    print("The light fades as last, at least you don't have to worry about finding your way home anymore.......")
    time.sleep(a)
    print("##--- GAME OVER- Cause: exploration hazard ---##")
    time.sleep(a)
    print("##--- PLEASE RESET THE GAME TO TRY AGAIN   ---##")
    time.sleep(a)
    sys.exit





### Main Function ###

print()
print()
print("     ######################")
print("     |                    |")
print("     |   DEEP SPACE III   |")
print("     |                    |")
print("     ######################")
print()
print()
time.sleep(a)
print("## DEEP SPACE III, but in TEXT! ###")
time.sleep(a)
print("##You awake in a crashed escape pod on a desolate world ##")
time.sleep(a)
print("## Before you lies the daunting task of finding your way back to Earth ##")
time.sleep(a)
print("## The journey will be hard, do you have what it takes? ##")
time.sleep(a)
print()
startGame = input("Would you like to start the game? (Y/N): ")
if startGame == "n" or startGame == "N":
    print("Maybe next time")
    time.sleep(3)
elif startGame == "y" or startGame == "Y":
    intro()