import  pygame
import  math
import  random
from    pygame.locals   import *
from    pygame          import mixer

WIDTH = 2000
HEIGHT = 1300
BLACK = (0,0,0)
FPS = 60
START_AGE = 20
DAY_AGE = 7300
CURRENT_AGE = DAY_AGE / 365
MAX_AGE = 65
MAX_DAY_AGE = 23725


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DEEP SPACE')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('player.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect =  self.image.get_rect()
        self.rect.center = (1000, 650)
    
    def update(self):
        global DAY_AGE
        global CURRENT_AGE
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        #Movement of player Sprite
        if keystate[pygame.K_a]:
            self.speedx = -2
            DAY_AGE = DAY_AGE + .25
            print(DAY_AGE)
            print(DAY_AGE/365)
        if keystate[pygame.K_d]:
            self.speedx = 2
            DAY_AGE = DAY_AGE + .25
            print(DAY_AGE)
            print(DAY_AGE/365)
        self.rect.x += self.speedx
        if keystate[pygame.K_w]:
            self.speedy = -2
            DAY_AGE = DAY_AGE + .25
            print(DAY_AGE)
            print(DAY_AGE/365)
        if keystate[pygame.K_s]:
            self.speedy = 2
            DAY_AGE = DAY_AGE + .25
            print(DAY_AGE)
            print(DAY_AGE/365)
        self.rect.y += self.speedy
                 
        #Map Constrainment        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0    
        if self.rect.top < 0:
            self.rect.top = 0         
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT 
            
    
        
class City(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('city1.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect =  self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        
def cityPrompt():
    print("Welcome to the city.  Before you is a sprawling metropolis...")
        
def spaceportPrompt():
    print('You have arrived at the planetary spaceport.  You can')
    print('(1) Upgarade your ship')
    print('(2) Buy Fuel')
    print('(3) Travel to another System')
    print('(4) Leave')
    print('What would you like to do?')
    
def cavePrompt():
    print("You have wandered upon an eery looking cave.  Just inside the entrance, you can see blood and bones.")
    
def quarryPrompt():
    print("You have made your way to the quarry.  It appears to be an old diamond mine.  The local guide offers to let you mine for a week for $100 credits.")
 
class Cave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cave.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect =  self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)       

class Quarry(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('diamond.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect =  self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
       
class Spaceport(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('spacestation.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect =  self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)    
       
def collision_detection():
    cityhit = pygame.sprite.spritecollide(player, citygroup, False)
    if cityhit:
        cityPrompt()
    
    spaceporthit = pygame.sprite.spritecollide(player, spaceportgroup, False)
    if spaceporthit:
        spaceportPrompt() 
    
    cavehit = pygame.sprite.spritecollide(player, cavegroup, False)
    if cavehit:
        cavePrompt()
        
    quarryhit = pygame.sprite.spritecollide(player, quarrygroup, False)
    if quarryhit:
        quarryPrompt()


all_sprites = pygame.sprite.Group()
citygroup =pygame.sprite.Group()
cavegroup =pygame.sprite.Group()
quarrygroup=pygame.sprite.Group()
spaceportgroup=pygame.sprite.Group()

player = Player()
city = City()
cave = Cave()
quarry = Quarry()
spaceport = Spaceport()
all_sprites.add(player, city, cave, quarry, spaceport)
citygroup.add(city)
cavegroup.add(cave)
quarrygroup.add(quarry)
spaceportgroup.add(spaceport)
age = 20


#Game Loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
             
    all_sprites.update() 
    collision_detection()   
    screen.fill((0,0,0))        
    all_sprites.draw(screen)     
    pygame.display.update()

pygame.quit()


  


 

