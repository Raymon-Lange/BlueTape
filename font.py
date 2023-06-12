import pygame

class Font():

    FONT_WIDTH = 8
    FONT_HEIGHT = 10

    def __init__(self, path) -> None:
        self.spaceing = 0
        self.charOrder = [['A','B','C','D','E','F','G','H','I','J'], #0
                          ['K','L','M','N','O','P','Q','R','S','T'],
                          ['U','V','W','X','Y','Z'],
                          ['0','1','2','3','4','5','6','7','8','9'],
                          ['.',',',':','?','!','(',')','+','=']]
        fontImg = pygame.image.load(path).convert_alpha()
        self.chars= {}
        for row in range(len(self.charOrder)):
            for col in range(len(self.charOrder[row])):
                surface = pygame.Surface((self.FONT_WIDTH, self.FONT_HEIGHT), pygame.SRCALPHA)
                rect = pygame.Rect(col * self.FONT_WIDTH, row * self.FONT_HEIGHT,  self.FONT_WIDTH, self.FONT_HEIGHT)
                surface.blit(fontImg,(0,0), rect)
                print(self.charOrder[row][col])
                self.chars[self.charOrder[row][col]]= pygame.transform.scale2x(surface)

    def draw(self, text , screen, x, y, offset_x):
        for char in text:
            if char != ' ':
                screen.blit(self.chars[char],( x + offset_x, y) )
            offset_x += self.FONT_WIDTH*2 + self.spaceing
            



