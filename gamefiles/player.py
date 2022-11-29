import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../images/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10,-16)
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.obstacle_sprites = obstacle_sprites
        
    def input(self):
        keystate = pygame.key.get_pressed()
                
        if keystate[pygame.K_w]:
            self.direction.y = -1
        elif keystate[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if keystate[pygame.K_d]:
            self.direction.x = 1
        elif keystate[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center
       
        
        
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: #player sprite moving right hitting the obstacle sprite left side
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: #player sprite moving left hitting the obstacle sprite right side
                        self.hitbox.left = sprite.hitbox.right    
        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: #player sprite moving down hitting the obstacle sprite top
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: #player sprite moving up hitting the obstacle sprite bottom
                        self.hitbox.top = sprite.hitbox.bottom
        
    def update(self):
        self.input()
        self.move(self.speed)