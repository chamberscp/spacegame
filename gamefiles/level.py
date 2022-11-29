import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
import random

class Level():
    def __init__(self):
            
        #Get the display surface        
        self.display_surface = pygame.display.get_surface()
        
        #Sprite Groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
    
        #Sprite setup
        self.create_map()
        
    def create_map(self):
        layouts = {
            'water':import_csv_layout('earth_water.csv'),
            'plants':import_csv_layout('earth_plants.csv'),
            'rocks':import_csv_layout('earth_rocks.csv'),
            'grass':import_csv_layout('earth_grass.csv')
            }
        graphics = {
            'water' : import_folder('../images/32X32.png'),
            'rocks' : import_folder('../images/32X32.png'),
            'plants' : import_folder('../images/32X32.png'),
            'grass' : import_folder('../images/32X32.png')
        }
        print(graphics)
        
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for column_index, column in enumerate(row):
                    if column != '-1':
                        x = column_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'water':  
                            Tile((x,y), [self.obstacle_sprites], 'water')
                        #if style == 'plants' : 
                            #surface = graphics[ 'plants' ] [int(column)] 
                            #Tile((x,y), [self.visible_sprites,self.obstacle_sprites], 'plants' , surface)
                        if style == 'rocks' :  
                            surf = graphics['rocks'][int(column)]
                            Tile((x,y), [self.visible_sprites,self.obstacle_sprites], 'rocks', surf)
                        
        self.player = Player((450,350),[self.visible_sprites], self.obstacle_sprites)    
    
    def run(self):
        #update and run the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        
        
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        #general setup for camera
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        self.floor_surf = pygame.image.load('../images/earth.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft =(0,0))
    
    def custom_draw(self, player):
        
        #Getting the screen offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)