import pygame
from block import Block
from traps import *
from item import Item


class Level():
    def __init__(self,screenHeight, screenWidth):
        self.width = screenWidth
        self.height = screenHeight
        self.levelObjects = self.loadLevel()
        self.obsticals = self.loadObsticals()
        self.objectives = self.loadObjectives()
        self.effects = []

    def loadLevel(self):
        block_size = 96

        #Rigth Side 
        floor = [Block(i * block_size, self.height - block_size, block_size,block_size, "Grass")
             for i in range(-self.width // block_size, (self.width * 2) // block_size)]
        
        floor.append(Block(0, self.height - block_size * 2, block_size,block_size, "Grass"))
        floor.append(Block(block_size * 3, self.height - block_size * 4, block_size,block_size, "Grass"))

        xpos = block_size * 11
        ypos = (self.height - block_size * 4 )
        for i in range(9):
            floor.append(Block(xpos, ypos, 36,32, "BrownSmallBox"))
            ypos += 32

        xpos = block_size * 14
        ypos = (self.height - block_size * 4 )
        for i in range(9):
            floor.append(Block(xpos, ypos, 36,32, "BrownSmallBox"))
            ypos += 32

        floor.append(Block((block_size * 4)-5, self.height - block_size * 4, 100,32, "BrownBar"))

        floor.append(Block((block_size * 5) -2, self.height - block_size * 3, 100,32, "BrownBar"))
        floor.append(Block((block_size * 6) -2, self.height - block_size * 3, 100,32, "BrownBar"))

        floor.append(Block((block_size * 7), self.height - block_size * 4, 100,32, "BrownBar"))

        floor.append(Block((block_size * 8) -2, self.height - block_size * 3, 100,32, "BrownBar"))
        floor.append(Block((block_size * 9) -2, self.height - block_size * 3, 100,32, "BrownBar"))

        floor.append(Block((block_size * 10), self.height - block_size * 4, 100,32, "BrownBar"))


        #Left Side

        floor.append(Block((block_size * -4)-5, self.height - block_size * 4, 100,32, "BrownBar"))

        floor.append(Block((block_size * -7), self.height - block_size * 4, 100,32, "BrownBar"))

        return floor
    
    def loadObsticals(self):
        obj = []
        block_size = 96

        fire = Fire(100, self.height - 96 - 64, 16, 32, "fire")
        fire.on()

        obj.append(fire)

        xPos = 96 *5 + 16
        for i in range(5):
            spike = Spike(xPos, self.height - 96 * 3 - 32,32,32,"spike")
            obj.append(spike)
            xPos += 32

        xPos = 96 *8 + 16
        for i in range(5):
            spike = Spike(xPos, self.height - 96 * 3 - 32,32,32,"spike")
            obj.append(spike)
            xPos += 32

        xPos = 96 * -1
        yPos = self.height - 96 - 55

        trampoline = Trampoline(xPos, yPos, 28,28,"trampoline")
        obj.append(trampoline)


        xPos = 96 *13 + 16
        trampoline1 = Trampoline(xPos, yPos, 28,28,"trampoline")
        obj.append(trampoline1)

        saw = Saw((block_size * -5) -2, (self.height - block_size * 4) + 32, 38,38, "saw")
        saw.on()
        path = [( (block_size * -7 )+50 , self.height - block_size * 4),( block_size * -4, self.height - block_size * 4)]
        saw.buildPath(path)
        obj.append(saw)


        return obj
    
    def loadObjectives(self):
        obj  = []

        xPos = 96 *3 + 16
        yPos = self.height - 96 - 64
        for i in range(5):
            apple = Item(xPos,yPos ,32,32,"Apple")
            obj.append(apple)
            xPos += 96

        xPos = 96 * 12
        melon = Item(xPos, yPos, 32,32 ,"Melon")
        melon.pointValue = 10
        obj.append(melon)

        return obj
    
    def loop(self):
        for obj in self.obsticals:
            obj.loop()

        for obj in self.objectives:
            obj.loop() 
        
        for obj in self.effects:
            obj.loop()
            if obj.finished:
                self.effects.remove(obj)


    def draw(self, screen, offsetX ):
        for block in self.levelObjects:
            block.draw(screen,offsetX)

        for obj in self.obsticals:
            obj.draw(screen, offsetX)

        for obj in self.objectives:
            obj.draw(screen, offsetX)

        for obj in self.effects:
            obj.draw(screen, offsetX)

    def addEffect(self, action):
        self.effects.append(action)
