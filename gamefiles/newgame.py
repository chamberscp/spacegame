import pygame
import sys
from pytmx.util_pygame import load_pygame
from settings import *
from level import Level

class Game():
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('DEEP SPACE II')
        tmx_data = load_pygame('../images/earthmap.tmx')
        print(dir(tmx_data))
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


##### story promts #####

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
    print('leave')
    print('Back to planet map')
    print('help')
    print('#############################')
    #earthCityOptions() #to be defined later

def spaceportPrompts():
    print('#############################')
    print('You arrive at the last spaceport on earth, your only way off your dying homeworld....')
    print('What would you like to do?')
    print('buy_fuel')
    print('leave the planet')
    print('Back to planet map')
    print('help')
    print('#############################')
    #spacePortOptions()
    # def spacePortOptions():
    #    option = input("> ")
    #    if option.lower() == ("buy_fuel"):
    #       buy_fuel() #def to be created later
    #    elif option.lower() == ("help"):
    #        #help_menu() 
    #    elif option.lower == ("leave"):
    #        sys.exit()
    #    while option.lower() not in ['buy_fuel', 'help', 'leave']:
    #        print("Please enter a listed command")
    #        option = input("> ")
    #        if option.lower() == ("buy_fuel"):
    #            #buy_fuel() #def to be created later
    #        elif option.lower() == ("help"):
    #            help_menu()
    #        elif option.lower() == ("leave"):
    #            #back_1_menu() #def to be created later

def quarryPrompt():
    print('#############################')
    print("You have made your way to the quarry.  It appears to be an old dilithium mine.  The local guide offers to let you mine for a week for $100 credits.")
    print('What would you like to do?')
    print('Mine reserouces  *list resrouce / age conversion rate')
    print('Back to planet map')
    print('help')
    print('#############################')
    


def cavePrompt():
    print("You have wandered upon an eery looking cave.  Just inside the entrance, you can see blood and bones.")