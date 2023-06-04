import pygame
from object import Object
from os.path import join

class Block(Object):
    def __init__(self, xPos, yPos, width, height , name):
        super().__init__(xPos, yPos, width, height, name)
        block = self.getBlock(width, height,name)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def getBlock(self, width, height, name):
        path = join("assets", "Terrain", "Terrain.png")
        return self.getSurface(width, height, path)

