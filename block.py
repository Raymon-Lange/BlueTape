import pygame
from object import Object
from os.path import join

BLOCKS = {"Grass": pygame.Rect(96, 0, 96, 96),
           "BrownBar": pygame.Rect(190, 0, 100, 32),
           "BrownSmallBox": pygame.Rect(190, 16, 36, 32)}

class Block(Object):
    def __init__(self, xPos, yPos, width, height , name):
        super().__init__(xPos, yPos, width, height, name)
        block = self.getBlock(width, height,name)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def getBlock(self, width, height, name):
        path = join("assets", "Terrain", "Terrain.png")
        return self.getSurface(width, height, path)

        #image = pygame.image.load(path).convert_alpha()
        #surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        #rect = BLOCKS[name]
        #surface.blit(image, (0, 0), rect)
        #return pygame.transform.scale2x(surface)

    

#190 240
#16