import pygame
from block import Block
from fire import Fire


class Level():
    def __init__(self,screenHeight, screenWidth):
        self.width = screenWidth
        self.height = screenHeight
        self.levelObjects = self.loadLevel()
        self.obsticals = self.loadObsticals()

    def loadLevel(self):
        block_size = 96
        floor = [Block(i * block_size, self.height - block_size, block_size,block_size, "Grass")
             for i in range(-self.width // block_size, (self.width * 2) // block_size)]
        
        floor.append(Block(0, self.height - block_size * 2, block_size,block_size, "Grass"))
        floor.append(Block(block_size * 3, self.height - block_size * 4, block_size,block_size, "Grass"))

        xpos = block_size * 3
        ypos = (self.height - block_size * 3 )
        for i in range(6):
            floor.append(Block(xpos, ypos, 36,32, "BrownSmallBox"))
            ypos += 32

        floor.append(Block((block_size * 4)-5, self.height - block_size * 4, 100,32, "BrownBar"))

        floor.append(Block((block_size * 5) -2, self.height - block_size * 3, 100,32, "BrownBar"))
        floor.append(Block((block_size * 6) -2, self.height - block_size * 3, 100,32, "BrownBar"))

        floor.append(Block((block_size * 7), self.height - block_size * 4, 100,32, "BrownBar"))



        return floor
    
    def loadObsticals(self):
        fire = Fire(100, self.height - 96 - 64, 16, 32, "fire")
        fire.on()

        return [fire]
    
    def loop(self):
        for obj in self.obsticals:
            obj.loop()


    def draw(self, screen, offsetX ):
        for block in self.levelObjects:
            block.draw(screen,offsetX)

        for obj in self.obsticals:
            obj.draw(screen, offsetX)
