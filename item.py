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
    FPS = 60
    #Hit Size 28 X 24

    def __init__(self, x, y, width, height, name="Box1"):
        super().__init__(x, y, width, height, name)
        self.item = Sprite()
        path = join("assets", "Items", "Boxes" ,name)
        self.item.loadSpriteSheet(path, width, height)
        self.image = self.item.allSprites["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.actionName = "Idle"
        self.isHit = False
        self.finished = False
        self.pointValue = 1
        self.fallCount = 0
        self.x_vel = 0
        self.y_vel = 0
        self.actionId = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def loop(self):
        if self.isHit:
            self.y_vel += min(1,  self.fallCount /60) * 1
            self.fallCount += 1 
            self.move(self.x_vel, self.y_vel)

            self.image = self.item.getSprite(self.actionName, self.actionId)
        else:
            sprites = self.item.allSprites[self.actionName]
            sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
            self.image = sprites[sprite_index]
            self.animation_count += 1

            if self.animation_count // self.ANIMATION_DELAY > len(sprites):
                self.animation_count = 0

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        
    def hit(self):
        self.isHit = True

        action = []
        leftBox = Box(self.rect.x, self.rect.y, self.width, self.height)
        leftBox.x_vel = 1
        leftBox.isHit = True
        leftBox.actionName = "Break"
        leftBox.actionId = 0
        action.append(leftBox)

        leftBox = Box(self.rect.x, self.rect.y, self.width, self.height)
        leftBox.x_vel = 1
        leftBox.y_vel = 1
        leftBox.isHit = True
        leftBox.actionName = "Break"
        leftBox.actionId = 1
        action.append(leftBox)

        leftBox = Box(self.rect.x, self.rect.y, self.width, self.height)
        leftBox.x_vel = 0
        leftBox.isHit = True
        leftBox.actionName = "Break"
        leftBox.actionId = 2
        action.append(leftBox)


        leftBox = Box(self.rect.x, self.rect.y, self.width, self.height)
        leftBox.x_vel =  -1
        leftBox.isHit = True
        leftBox.actionName = "Break"
        leftBox.actionId = 3
        action.append(leftBox)

        return action

