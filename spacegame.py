'''import  pygame
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
    getIntro()'''
 
from    enum            import Enum     
import  pygame
import  pygame.freetype
from    pygame.locals   import *
from    pygame          import mixer
from    pyfiglet        import Figlet
from    pygame.sprite   import Sprite
from    pygame.rect     import Rect

# Global variables
user_name = []
BLUE = (0,0,255)
WHITE = (255, 255, 255)

def create_text(text, font_size, text_rgb, bg_rgb):
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _= font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

    
class UIElement(Sprite):
    
    def __init__(self, center_pos, text, font_size, text_rgb, bg_rgb, action=None):
                     
        self.mouse_over = False
        
        default_image = create_text(text, font_size, text_rgb, bg_rgb)
        
        highlighted_image = create_text(text, font_size * 2, text_rgb, bg_rgb)
        
        self.images = [default_image, highlighted_image]
        self.images = [default_image, highlighted_image]
        self.rects  = [
            default_image.get_rect(center=center_pos), 
            highlighted_image.get_rect(center=center_pos)]
        
        self.action = action
        
        super().__init__()
    
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]
    
    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
    
    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)

def main():
    pygame.mixer.pre_init()
    pygame.init()
    screen = pygame.display.set_mode((2000,2000))
    window = pygame.display.set_caption('SPACE GAME')
    bg_img = pygame.image.load('space.png')
    bg_img = pygame.transform.scale(bg_img,(2000,2000))
    game_state = gameState.TITLE
    
    while True:
        if game_state == gameState.TITLE:
            game_state = title_screen(screen)
        
        if game_state == gameState.NEWGAME:
            game_state = play(screen)
            
        if game_state == gameState.QUIT:
            pygame.quit()
            return

def title_screen(screen):
    title_btn = UIElement(
        center_pos=(1000, 300),
        font_size=100,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="SPACE GAME",
        action=gameState.TITLE,
    )
    
    start_btn = UIElement(
        center_pos=(1000, 700),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start",
        action=gameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_pos=(1000, 800),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=gameState.QUIT,
    )

    buttons = [title_btn, start_btn, quit_btn]
    
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()
        
def play(screen):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=gameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()
    
    
    #mixer.init()
    #mixer.music.load('desolateworld.ogg')
    #mixer.music.play()
    #pygame.time.wait(273) 
    
    running = True
    while running:
        mouse_up = False              
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)               
        
        ui_action = quit_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return
        quit_btn.draw(screen)
        #uielement.update(pygame.mouse.get_pos())
        #uielement.draw(screen)
        pygame.display.flip()  
        
class gameState():
    QUIT = -1  
    TITLE = 0
    NEWGAME = 1

if __name__ == "__main__":
    main()
