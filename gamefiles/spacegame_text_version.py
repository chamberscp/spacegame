import cmd
import sys
import time
import os

#0 = empty wastes, #1 = spaceport, #2 = store, #3 = mine
planetearth = [[0, 0, 0, 0, 1],
               [0, 0, 0, 0, 0],
               [0, 0, 2, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 3],
]

class Player:
    def __init__(self):
        self.name = ''
        self.money = 0
        self.wallet = 0
        self.planet = 0
        self.planetSize = 5 
        self.fuel = 0
        self.age = 20
        self.location = [0,0]
        self.game_over = False
        
    #pos setters
    def moveDirection(self, dir):
        if dir == "right":
            self.location[1] += 1 #do out of bounds check
            if self.location[1] >= self.planetSize:
               self.location[1] = 0
        elif dir == "left":
            self.location[1] -= 1
            if self.location[1] < 0:
               self.location[1] = self.planetSize
        elif dir == "down":
            self.location[0] += 1
            if self.location[0] >= self.planetSize:
               self.location[0] = 0
        elif dir == "up":
            self.location[0] -= 1
            if self.location[0] < 0:
               self.location[0] = self.planetSize
                      

    def getLocation(self):
        return self.location

    def addMoney(self, amt):
        self.wallet += amt

    def takeMoney(self, amt):
        if amt > self.wallet:
           return False
        else:
            self.wallet -= amt
            return True

    def addFuel(self, amt):
        self.fuel += amt

    def burnFuel(self, amt):
        self.fuel -= amt

    def setName(self, n):
        self.name = n
    
    def setPlanet(self, p):
        self.planet = p
    
    def setPlanetSize(self, s):
        self.planetSize = s
    
    def setAge(self, a):
        self.age = a


# getters 
    def getLocation(self):
        return self.location

    def getMoney(self):
        return self.money

    def getName(self):
        return self.name

    def getPlanet(self):
        return self.planet

    def getPlanetSize(self):
        return self.planetSize

    def getAge(self):
        return self.age
    
    def getFuel(self):
        return self.fuel

player = Player()

#### Main Menu ####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() #new main
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a listed command")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


def title_screen():
    os.system('cls')
    print('#####################################')
    print('## Welcome to spacegame.test RPG! ###')
    print('#####################################')
    print('              - Play -               ')
    print('              - Help -               ')
    print('              - Quit -               ')
    print('#####################################')
    title_screen_selections()

def help_menu():
    print('#####################################    ')
    print('## Welcome to spacegame.test RPG! ###    ')
    print('#####################################    ')
    print('- Use up, Down, Left, and right to move  ')
    print('  -  type your commands to do them       ')
    print(' use "look" to check the area you are in ')
    print('  -  Working on the Rest!                ')
    title_screen_selections()

def getCommand():
    global player
    acceptable_commands = ['move', 'go',]
    print("What would you like to do?\n")
    command = input("> ").lower()

    if command.split()[0] in acceptable_commands:
        if command.split()[0] in ['move', 'go']:
            if len(command.split()) == 2:
                direction = command.split()[1]
            else:
                print("What direction would you like to go?\n")
                direction = input("> ")
            player.moveDirection(direction)

    print(player.getLocation())





#  Game Funtionalty #


def main_game_loop():
    while player.game_over is False:
        printMap()
        getCommand()
        #tbd
    # here is where we will define goals, fuel, money, endings ect
        

def start_game():
    os.system('cls')

    #get player name
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    player.setName(player_name)   
    
    main_game_loop()





def printMap():
    row = "  ---------------------"
    print("    0   1   2   3   4   5  ")
    print(row)
    print("0 | {} | {} | {} | {} | {} |".format(planetearth[0][0], planetearth[0][1],planetearth[0][2],planetearth[0][3],planetearth[0][4]))
    print(row)
    print("1 | {} | {} | {} | {} | {} |".format(planetearth[1][0], planetearth[1][1],planetearth[1][2],planetearth[1][3],planetearth[1][4]))
    print(row)
    print("2 | {} | {} | {} | {} | {} |".format(planetearth[2][0], planetearth[2][1],planetearth[2][2],planetearth[2][3],planetearth[2][4]))
    print(row)
    print("3 | {} | {} | {} | {} | {} |".format(planetearth[3][0], planetearth[3][1],planetearth[3][2],planetearth[3][3],planetearth[3][4]))
    print(row)
    print("4 | {} | {} | {} | {} | {} |".format(planetearth[4][0], planetearth[4][1],planetearth[4][2],planetearth[4][3],planetearth[4][4]))
    print(row)
    print("You are currently at {}".format(player.getLocation()))
    
title_screen()
   


#0 = empty wastes, #1 = spaceport, #2 = store, #3 = mine

