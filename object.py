import pygame

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