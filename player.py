import pygame

class Player(pygame.sprite.Sprite):
    COLOR = (255,0,0)
    GAVITY = 1

    def __init__(self, x,y,width, height):
        self.rect = pygame.Rect(x,y,width,height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fallCount = 0 #how long the player have been falling

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def moveLeft(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def moveRight(self, vel):
        self.x_vel = vel
        if self.direction != "rigth":
            self.direction = "right"
            self.animation_count = 0
        
    def loop(self, fps):
        self.y_vel += min(1, self.fallCount /fps) * self.GAVITY

        self.move(self.x_vel, self.y_vel)

        self.fallCount += 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.COLOR, self.rect )
