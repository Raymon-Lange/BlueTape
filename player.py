import pygame
from sprite import Sprite

class Player(pygame.sprite.Sprite):
    COLOR = (255,0,0)
    GRAVITY = 1
    ANIMATION_DELAY = 5

    def __init__(self, x,y,width, height):
        super().__init__()
        self.rect = pygame.Rect(x,y,width,height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animationCount = 0
        self.fallCount = 0 #how long the player have been falling
        self.sprites = Sprite()
        self.jumpCount = 0
        self.hit = False
        self.hitCount = 0
        self.isFly = False

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def moveLeft(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animationCount = 0

    def moveRight(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animationCount = 0

    def jump(self, scale=8):
        self.y_vel = -self.GRAVITY * scale
        self.animation_count = 0
        self.jumpCount += 1
        if self.jumpCount == 1:
            self.fall_count = 0
        
    def loop(self, fps):
        if self.isFly:
            self.y_vel += min(1, ((self.fallCount /fps) * self.GRAVITY ) /4 )
        else:
            self.y_vel += min(1, self.fallCount /fps) * self.GRAVITY

        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hitCount += 1
        if self.hitCount > fps * 2:
            self.hit = False
            self.hitCount = 0

        self.fallCount += 1
        self.updateSprite()

    def draw(self, screen, offset_x):
        screen.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))

    def loadSprite(self,path, width, height, direction = False):
        self.sprites.loadSpriteSheet(path, width, height, direction)

    def updateSprite(self):
        spriteSheet = "idle"
        if self.hit:
            spriteSheet = "hit"
#        elif self.x_vel == 0 and self.y_vel > 0:
#            spriteSheet ="wall_jump"
        elif self.y_vel < 0:
            if self.jumpCount == 1:
                spriteSheet = "jump"
            elif self.jumpCount == 2:
                spriteSheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 3:
            spriteSheet = "fall"
        elif self.x_vel != 0:
            spriteSheet = "run"


        animationName = spriteSheet + "_" + self.direction
        animationIndex = (self.animationCount // self.ANIMATION_DELAY) % len(self.sprites.allSprites[animationName])
        self.sprite = self.sprites.getSprite(animationName, animationIndex)
        self.animationCount += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def landed(self):
        self.fallCount = 0
        self.y_vel = 0
        self.jumpCount = 0
        self.isFly = False

    def hitHead(self):
        self.fallCount = 0
        self.y_vel *= -1

    def takeDamage(self):
        self.hit = True
