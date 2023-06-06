import pygame
from object import Object 
from sprite import Sprite


class Item(Object):
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height, name)
        self.apple = Sprite()
        self.apple.loadSpriteSheet("Items", "Fruits", width, height)
        self.image = self.apple.allSprites[self.name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.isCollected = False
        self.finished = False
        self.pointValue = 1

    def loop(self):
        sprites = self.apple.allSprites[self.name]
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