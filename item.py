import pygame
from os.path import isfile, join
from object import Object 
from sprite import Sprite


class Item(Object):
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height, name)
        self.item = Sprite()
        path = join("assets", "Items", "Fruits")
        self.item.loadSpriteSheet(path, width, height)
        self.image = self.item.allSprites[self.name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.isCollected = False
        self.finished = False
        self.pointValue = 1

    def loop(self):
        sprites = self.item.allSprites[self.name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
            self.finished = True

    def collected(self):
        self.isCollected = True

class Box(Object):
    ANIMATION_DELAY = 5
    #Hit Size 28 X 24

    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height, name)
        self.item = Sprite()
        path = join("assets", "Items", "Boxes" ,"Box1")
        self.item.loadSpriteSheet(path, width, height)
        self.image = self.item.allSprites[self.name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.isCollected = False
        self.finished = False
        self.pointValue = 1

    def loop(self):
        sprites = self.item.allSprites[self.name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
            self.finished = True

    def collected(self):
        self.isCollected = True
