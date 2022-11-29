import sys
import time

a = 2
b = 0.2
c = 0.08

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
        time.sleep(b)
    time.sleep(1.0)
    print()
    print()
    print("As you venture inside you see the cave splits off into several tunnels....")
    time.sleep(a)
    print("Three paths are revealed:")
    time.sleep(a)
    print()
    print("Path #1: Go down the Center path, *you see what looks to be claw marks on the walls*....")
    time.sleep(a)
    print("Path #2: Go down the right path, *you think to yourself you heard faint sounds coming from this direction*....")
    time.sleep(a)
    print("Path #3: turn around and leave the cave....")
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
print("You awake in a crashed escape pod on a desolate world")
time.sleep(a)
print("Before you lies the daunting task of finding your way back to Earth")
time.sleep(a)
print("The journey will be hard, do you have what it takes?")
time.sleep(a)
print()
startGame = input("Would you like to start the game? (Y/N): ")
if startGame == "n" or startGame == "N":
    print("Maybe next time")
    time.sleep(3)
elif startGame == "y" or startGame == "Y":
    intro()