import pygame
from csv import reader

from os import walk
from os.path import join
from item import Item
from traps import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,size,x,y):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self,shift):
        self.rect.x += shift
                
    def draw(self, screen, offset_x):
        screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))

class StaticTile(Tile):
	def __init__(self,size,x,y,surface):
		super().__init__(size,x,y)
		self.image = surface 

class Level:

    def __init__(self, level_data,screenHeight, screenWidth):
        self.width = screenWidth
        self.height = screenHeight
        self.tile_size = 16

        # terrain setup
        terrain_layout = self.import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

        # Fruits setup
        fruit_layout = self.import_csv_layout(level_data['fruits'])
        self.fruit_sprites = self.create_tile_group(fruit_layout,'fruits')

        #Traps setup
        trap_layout = self.import_csv_layout(level_data['traps'])
        self.trap_sprites = self.create_tile_group(trap_layout,'traps')

    def import_folder(self, path):
        surface_list = []
        for _,__,image_files in walk(path):
            for image in image_files:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
        return surface_list

    def import_csv_layout(self, path):
        terrain_map = []
        with open(path) as map:
            level = reader(map,delimiter = ',')
            for row in level:
                terrain_map.append(list(row))
            return terrain_map

    def import_cut_graphics(self,path):
        surface = pygame.image.load(path).convert_alpha()
        tile_num_x = int(surface.get_size()[0] / self.tile_size)
        tile_num_y = int(surface.get_size()[1] / self.tile_size)

        cut_tiles = []
        for row in range(tile_num_y):
            for col in range(tile_num_x):
                x = col * self.tile_size
                y = row * self.tile_size
                new_surf = pygame.Surface((self.tile_size,self.tile_size),flags = pygame.SRCALPHA)
                new_surf.blit(surface,(0,0),pygame.Rect(x,y,self.tile_size,self.tile_size))
                cut_tiles.append(new_surf)
        
        return cut_tiles
    
    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val != '-1':
                    x = col_index * self.tile_size
                    y = row_index * self.tile_size

                    if type == 'terrain':
                        terrain_tile_list = self.import_cut_graphics(path = join( "assets", "Terrain", "Terrain.png"))
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(self.tile_size,x,y,tile_surface)

                    if type == 'fruits':
                        if val == "0": sprite = Item(x,y-16,32,32,"Apple")
                        if val == "1": sprite = Item(x,y-16,32,32,"Bananas")
                        if val == "2": sprite = Item(x,y-16,32,32,"Cherries")
                        if val == "3": sprite = Item(x,y-16,32,32,"Kiwi")
                        if val == "4": sprite = Item(x,y-16,32,32,"Melon")
                        if val == "5": sprite = Item(x,y-16,32,32,"Orange")
                        if val == "6": sprite = Item(x,y-16,32,32,"Pineapple")
                        if val == "7": sprite = Item(x,y-16,32,32,"Strawberry")

                    if type == 'traps':
                        if val == "0": sprite = Spike(x,y,32,32,"spike")
                        if val == "1": sprite = Item(x,y-16,32,32,"Bananas")
                        if val == "2": sprite = Item(x,y-16,32,32,"Cherries")
                        if val == "3": sprite = Item(x,y-16,32,32,"Kiwi")
                        if val == "4": sprite = Fan(x, y+8, 24,8,"fan")
                        if val == "5": sprite = Item(x,y-16,32,32,"Orange")
                        if val == "6": sprite = Item(x,y-16,32,32,"Pineapple")
                        if val == "7": sprite = Item(x,y-16,32,32,"Strawberry")
                    
                    sprite_group.add(sprite)
		
        return sprite_group
    
    def draw(self, screen, offsetX):
        for block in self.terrain_sprites:
            block.draw(screen,offsetX)

        for block in self.fruit_sprites:
            block.draw(screen,offsetX)

        for block in self.trap_sprites:
            block.draw(screen, offsetX)
