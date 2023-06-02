import random, os
import pygame
from os import listdir
from os.path import isfile, join

class Game:
    def __init__(self):
        self.gameOver = False
        self.width = 800
        self.height = 600

    def getBackground(self, name):
        image = pygame.image.load(join("assets", "Background", name))
        x, y, imageWidth, imageHeight = image.get_rect()
        tiles = []
        for i in range(self.width // imageWidth + 1):
            for j in range(self.height // imageHeight + 1):
                pos = ( i * imageWidth, j * imageHeight)
                tiles.append(pos)
        
        return tiles, image
    
    def draw(self, screen):
        background, image = self.getBackground("Blue.png")

        for tile in background:
            screen.blit(image, tile)


