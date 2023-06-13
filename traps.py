import pygame
from object import Object
from os.path import join
from sprite import Sprite

class Fire(Object):
    ANIMATION_DELAY = 5

    def __init__(self, xPos, yPos, width, height , name) -> None:
        super().__init__(xPos, yPos, width, height, name)
        self.fire = Sprite()
        self.fire.loadSpriteSheet("Traps", "Fire", width, height)
        self.image = self.fire.allSprites["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire.allSprites[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


class Spike(Object):
    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height, name)
        block = self.getBlock(width, height,name)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def getBlock(self, width, height, name):
        path = join("assets", "Traps", "Spikes", "idle.png")
        return self.getSurface(width, height, path)
    
    def loop(self):
        pass
