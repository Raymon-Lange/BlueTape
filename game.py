import random, os
import pygame
from os import listdir
from os.path import isfile, join

class Game:
    def __init__(self):
        self.gameOver = False
        self.width = 0
        self.height = 0

        path = os.path.join("assets", "Hud","TopHUD.png")

        self.hud = self.getHud(path)

    def getBackground(self, name):
        image = pygame.image.load(join("assets", "Background", name))
        x, y, imageWidth, imageHeight = image.get_rect()
        tiles = []
        for i in range(self.width // imageWidth + 1):
            for j in range(self.height // imageHeight + 1):
                pos = ( i * imageWidth, j * imageHeight)
                tiles.append(pos)
        
        return tiles, image
    
    def getHud(self, name):
        image = pygame.image.load(name)
        return image
    
    def draw(self, screen):
        background, image = self.getBackground("Blue.png")

        for tile in background:
            screen.blit(image, tile)

        screen.blit(self.hud,(0,0))


    def handleVerticalCollision(self, player, objects, dy):
        collided_objects = []
        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                if dy > 0:
                    player.rect.bottom = obj.rect.top
                    player.landed()
                elif dy < 0:
                    player.rect.top = obj.rect.bottom
                    player.hitHead()

                collided_objects.append(obj)
                break

        return collided_objects
    
    def collide(self, player, objects, dx):
        #STEP: Moving the playforward in the fucture by currect vel
        player.move(dx, 0)
        player.update()
        collided_object = None

        #STEP: Check if we collide
        for obj in objects:
            if pygame.sprite.collide_mask(player, obj):
                collided_object = obj
                break

        #STEP: Move the player back. 
        player.move(-dx, 0)
        player.update()
        return collided_object


