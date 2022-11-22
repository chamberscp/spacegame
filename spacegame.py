import  pygame
from    pygame.locals   import *
from    pygame          import mixer
from    pyfiglet        import Figlet

# Global variables
user_name = []

#pygame setup
pygame.init()
width = 2000
height = 2000
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('space.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

mixer.init()
mixer.music.load('desolateworld.ogg')
mixer.music.play()

pygame.display.set_caption('SPACE GAME')

running = True
while running:
    window.blit(bg_img,(0,0))
    for event in pygame.event.get():
        if event.type == quit:
            running = False
    pygame.display.update()
pygame.quit()



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
     

