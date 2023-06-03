import pygame
from object import Object
from os.path import join

class Block(Object):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size, None)
        block = self.get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def get_block(self, size):
        path = join("assets", "Terrain", "Terrain.png")
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(96, 0, size, size)
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale2x(surface)
    

