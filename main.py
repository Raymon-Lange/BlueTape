import os,sys, random, math
import pygame
from os import listdir
from os.path import isfile, join
from game import Game
from level import Level
from player import Player

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("BlueTape")

BG_COLOR = (255,255,255)
WIDTH, HEIGHT = 800, 600
FPS = 80
PLAYER_VELOCITY = 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main(screen):
    run = True

    #STEP: INIT Game Data
    game = Game()
    game.width = WIDTH
    game.height = HEIGHT

    player = Player(100,100,50,50)
    player.loadSprite("MainCharacters", "NinjaFrog", 32, 32, True)

    level = Level(HEIGHT, WIDTH)
    level.loadLevel()

    while run:
        clock.tick(FPS)

        #STEP: stop x vel everyone
        player.x_vel = 0
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False #Gets up out of the loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jumpCount < 2:
                    player.jump()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player.moveLeft(PLAYER_VELOCITY)
        if keys[pygame.K_d]:
            player.moveRight(PLAYER_VELOCITY)


        #STEP: Update Pos
        player.loop(FPS)
        game.handleVerticalCollision(player, level.LevelObjects, player.y_vel)

        #STEP: Draw Games
        game.draw(screen)

        level.draw(screen)

        player.draw(screen)
        pygame.display.update()

    # STEP:Clear up 
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main(screen)

