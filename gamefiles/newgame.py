import pygame
import sys

from settings import *
from level import Level

class Game():
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('DEEP SPACE II')
       
        self.clock = pygame.time.Clock()
        
        self.level = Level()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()

#player class and related get/set funtions
class Player:
    def __init__(self):
        self.name = ''
        self.money = 0
        self.planet = 0
        self.fuel = 0
        self.age = 20
        self.game_over_age = False

    def game_over_age(): True
    print("Though you tried your best and put countless years into this journey, at long last you have succumb \n \
         and die peacefully of old age as you lay asleep in your bed")
    # maybe just pass sys.exit and close game?


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
    

# getters 
    def getLocation(self):
        return self.location

    def getMoney(self):
        return self.money

    def getName(self):
        return self.name

    def getPlanet(self):
        return self.planet
    
    def getFuel(self):
        return self.fuel

player = Player()




##### story promts #####

def buy_fuel(): pass
def ReturntoMap(): pass
def leavePlanet(): pass
def help_menu(): pass
def mine(): pass
def loot(): pass

def startgameprompt():
    print('#############################')
    print('# You awake from your cryo-pod, doing your best to shrug off the overwelming disorientation it leaves you with ')
    print('# Oddly you see no one else in sight, just the charred and wrecked remains of the cyro facility meant to save you from the worst of it ')
    print('# you look around, finding no signs of life, after a while you find a AI info terminal, you ask it where the others are.')
    print('# "97%\\ of the remmaining human populaiton has already fled to New Eden, they left 38.5 years ago, only the most bitter of holdouts remain" ')
    print('# you missed the boat, unsure of what malfuntion caused your cyro pod to not open on time, or why no one got you out, you realize you have been left behind......')
    print('# with Earth and the entire Sol system devastated and near lifeless, you realize you must do whatever it takes to escape the the cradle of humanity, and reach the promised safety of New Eden')
    print('# *display current stats: age, fuel, money*') #to be shown via funtion later
    print('# your mission: ') #mission statement here
    print('#############################')



def cityPrompt():
    print('#############################')
    print('Welcome to the city.  Before you lies Bastion, the last remaining human city on Earth....')
    print('What would you like to do?')
    print('buy_fuel')
    print('Back to planet map')
    print('help')
    print('#############################')
    CityOptions() #to be defined later
    def CityOptions():
        option = input("> ")
        if option.lower() == ("buy_fuel"):
           buy_fuel() #def to be created later
        elif option.lower() == ("help"):
            help_menu() 
        elif option.lower == ("back"):
             ReturntoMap() #to be defined later
        while option.lower() not in ['buy_fuel', 'help', 'back']:
            print("Please enter a listed command")
            option = input("> ")
            if option.lower() == ("buy_fuel"):
                buy_fuel() #def to be created later
            elif option.lower() == ("help"):
                help_menu()
            elif option.lower() == ("back"):
                ReturntoMap() #to be defined later



def spaceportPrompts():
    print('#############################')
    print('You arrive at the last spaceport "Angel gate" on earth, your only way off your dying homeworld....')
    print('What would you like to do?')
    print('buy_fuel')
    print('leave the planet')
    print('Back to planet map')
    print('help')
    print('#############################')
    '''spacePortOptions()
    def spacePortOptions():
        option = input("> ")
        if option.lower() == ("buy_fuel"):
           buy_fuel() #def to be created later
        elif option.lower() == ("help"):
            help_menu() 
        elif option.lower() == ("back"):
            ReturntoMap() #to be defined later
        elif option.lower == ("Leave"):
<<<<<<< Updated upstream
                leavePlanet(): #to be defined later 
=======
<<<<<<< HEAD
              leavePlanet()
              #to be defined later 
=======
                leavePlanet(): #to be defined later 
>>>>>>> e229973bc4f2a9a0e43c70e4d61c6614378b834f
>>>>>>> Stashed changes
        while option.lower() not in ['buy_fuel', 'help', 'leave']:
            print("Please enter a listed command")
            option = input("> ")
        if option.lower() == ("buy_fuel"):
                buy_fuel() #def to be created later
        elif option.lower() == ("help"):
             help_menu()
        elif option.lower() == ("leave"):
<<<<<<< Updated upstream
                leavePlanet(): #to be defined later pass'''
=======
<<<<<<< HEAD
                leavePlanet() #to be defined later pass
=======
                leavePlanet(): #to be defined later pass'''
>>>>>>> e229973bc4f2a9a0e43c70e4d61c6614378b834f
>>>>>>> Stashed changes





def quarryPrompt():
    print('#############################')
    print("You have made your way to the quarry.  It appears to be an old dilithium mine.  The local guide offers to let you mine for a week for $100 credits.")
    print('What would you like to do?')
    print('Mine reserouces  *list resrouce / age conversion rate')
    print('Back to planet map')
    print('help')
    print('#############################')
    QuarryOptions()
    def QuarryOptions():
        option = input("> ")
        if option.lower() == ("Mine"):
           mine() #def to be created later
        elif option.lower() == ("help"):
            help_menu() 
        elif option.lower == ("back"):
            ReturntoMap()
        while option.lower() not in ['Mine', 'help', 'leave']:
            print("Please enter a listed command")
            option = input("> ")
            if option.lower() == ("Mine"):
                mine() #def to be created later
            elif option.lower() == ("help"):
                help_menu() 
            elif option.lower() == ("back"):
                ReturntoMap()
    
    


def cavePrompt():
    print('#############################')
    print("You have wandered upon an eery looking cave.  Just inside the entrance, \n \
        you can see dried blood and the bones of those who tried to hide from the devastation,\n \
        tough grizzly, you think to yourself, surely there must be credits or valuables you can loot to buy fuel in there....")
    print('#############################')
    print('What would you like to do?')
    print('Mine reserouces  *list credit gather rate / age conversion rate')
    print('Back to planet map')
    print('help')
    print('#############################')
    CaveOptions()
    def CaveOptions():
        option = input("> ")
        if option.lower() == ("loot"):
           mine() #def to be created later
        elif option.lower() == ("help"):
            help_menu() 
        elif option.lower == ("back"):
            ReturntoMap()
        while option.lower() not in ['loot', 'help', 'back']:
            print("Please enter a listed command")
            option = input("> ")
            if option.lower() == ("loot"):
                loot() #def to be created later
            elif option.lower() == ("help"):
                help_menu() 
            elif option.lower() == ("back"):
                ReturntoMap()