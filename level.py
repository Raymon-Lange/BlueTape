import pygame
from block import Block

class Level():
    def __init__(self,screenHeight, screenWidth):
        self.width = screenWidth
        self.height = screenHeight
        self.LevelObjects = self.loadLevel()

    def loadLevel(self):
        block_size = 96
        floor = [Block(i * block_size, self.height - block_size, block_size)
             for i in range(-self.width // block_size, (self.width * 2) // block_size)]
        
        floor.append(Block(0, self.height - block_size * 2, block_size))
        floor.append(Block(block_size * 3, self.height - block_size * 4, block_size))
        
        return floor

    def draw(self, screen, offsetX ):
        for block in self.LevelObjects:
            block.draw(screen,offsetX)
