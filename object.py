import pygame

OBJECTS = {"Grass": pygame.Rect(96, 0, 96, 96),
           "BrownBar": pygame.Rect(190, 0, 100, 32),
           "BrownSmallBox": pygame.Rect(190, 16, 36, 32)}

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)  # supports transparent images
        self.width = width
        self.height = height
        self.name = name

    def draw(self, screen, offset_x):
        screen.blit(self.image, (self.rect.x - offset_x, self.rect.y))

    def getSurface(self, width, height, path):
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = OBJECTS[self.name]
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale2x(surface)