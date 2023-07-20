import os,sys, random, math
import pygame
from os import listdir
from os.path import isfile, join

class Sprite():
    def __init__(self):
        self.allSprites = {}

    def flip(self, sprites):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
    
    def loadSpriteSheet(self, path, width, height, direction=False):
        images = [f for f in listdir(path) if isfile(join(path, f))]

        for image in images: 
            spriteSheet = pygame.image.load(join(path,image)).convert_alpha()

            sprites= []
            for i in range(spriteSheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(spriteSheet,(0,0), rect)
                sprites.append(pygame.transform.scale2x(surface))
        
            if direction:
                self.allSprites[image.replace(".png", "") + "_right"] = sprites
                self.allSprites[image.replace(".png", "") + "_left"] = self.flip(sprites)
            else:
                self.allSprites[image.replace(".png", "")] = sprites

    def getSprite(self, name, pos):
        return self.allSprites[name][pos]
    
    def getAllSprint(self):
        return self.allSprites
