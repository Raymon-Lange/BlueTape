import pygame
from object import Object
from os.path import join
from sprite import Sprite
from random import randint

class Fire(Object):
    ANIMATION_DELAY = 5

    def __init__(self, xPos, yPos, width, height , name) -> None:
        super().__init__(xPos, yPos, width, height, name)
        self.fire = Sprite()
        path = join("assets","Traps", "Fire")
        self.fire.loadSpriteSheet(path, width, height)
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
        image = self.getBlock(width, height,name)
        self.image.blit(image, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def getBlock(self, width, height, name):
        path = join("assets", "Traps", "Spikes", "idle.png")
        return self.getSurface(width, height, path)
    
    def loop(self):
        pass


class Trampoline(Object):
    ANIMATION_DELAY = 5
    #28X28
    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height, name)
        
        self.trampoline = Sprite()
        path = join("assets","Traps", "Trampoline")
        self.trampoline.loadSpriteSheet(path, width, height)
        self.image = self.trampoline.allSprites["Idle"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Idle"

    def on(self):
        self.animation_name = "Jump"

    def off(self):
        self.animation_name = "Idle"

    def loop(self):
        sprites = self.trampoline.allSprites[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
            self.off()


class Saw(Object):
    ANIMATION_DELAY = 3
    #28X28
    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height, name)
        
        self.saw = Sprite()
        path = join("assets","Traps", "Saw")
        self.saw.loadSpriteSheet(path, width, height)
        self.image = self.saw.allSprites["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "on"
        self.xVel = 0
        self.yVel = 0
        self.path = None
        self.pathPos = 0
    
    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.saw.allSprites[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

        self.move()

    def buildPath(self, path):
        self.path = path
        self.dest = path[0]
    
    def move(self):
        #STEP: Check if we have a path 
        if self.path == None:
            return 

        #STEP: Check if at the location 
        xPos = self.rect.x
        yPos = self.rect.y

        atXDest = (xPos == self.dest[0])
        atYDest = (yPos == self.dest[1])

        #STEP: if at location pick a new location

        if atXDest and atYDest:
            if self.pathPos == len(self.path)-1:
                self.pathPos = 0
            else:
                self.pathPos += 1

            self.dest = self.path[self.pathPos]

        if xPos > self.dest[0]:
            self.xVel = -1
        elif xPos < self.dest[0]:
            self.xVel = 1

        if yPos > self.dest[1]:
            self.yVel = -1
        elif yPos < self.dest[1]:
            self.yVel = 1


        #STEP: move toward location
        self.rect.x += self.xVel
        self.rect.y += self.yVel

class Platform(Object):
    ANIMATION_DELAY = 5
    GRAVITY = 1
    #32X10
    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height, name)
        
        self.saw = Sprite()
        path = join("assets","Traps", "Falling Platforms")
        self.saw.loadSpriteSheet(path, width, height)
        self.image = self.saw.allSprites["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"
        self.yVel = 0
        self.yOrginalLocation = y
        self.timeBeforeFall = 10
        self.fallCount = 0
        self.falling = False
    
    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.saw.allSprites[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

        self.move()

    def buildPath(self, path):
        self.path = path
        self.dest = path[0]
    
    def move(self):
        if self.animation_name == "off":
            if self.timeBeforeFall <= 0:
                self.yVel += min(1, self.fallCount /60) * self.GRAVITY
                self.rect.y += self.yVel
                self.fallCount += 1
            else:
                self.timeBeforeFall = self.timeBeforeFall - 1
        else:
            if self.animation_count // self.ANIMATION_DELAY == 0:
                self.rect.y = self.yOrginalLocation  + randint(-1,1)

class Fan(Object):
    ANIMATION_DELAY = 5
    #24x8
    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height, name)
        
        self.trampoline = Sprite()
        path = join("assets", "Traps", "Fan")
        self.trampoline.loadSpriteSheet(path, width, height)
        self.image = self.trampoline.allSprites["Off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "Off"

    def on(self):
        self.animation_name = "On"

    def off(self):
        self.animation_name = "Off"

    def loop(self):
        sprites = self.trampoline.allSprites[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


