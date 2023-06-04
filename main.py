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
WIDTH, HEIGHT = 800, 700
FPS = 80
PLAYER_VELOCITY = 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main(screen):
    run = True
    offset_x = 0
    scroll_area_width = 200

    #STEP: INIT Game Data
    game = Game()
    game.width = WIDTH
    game.height = HEIGHT

    player = Player(50,50,50,50)
    player.loadSprite("MainCharacters", "NinjaFrog", 32, 32, True)
    player.loop(FPS)

    level = Level(HEIGHT, WIDTH)
    level.loadLevel()



    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False #Gets up out of the loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jumpCount < 2:
                    player.jump()
        
        #STEP: stop x vel because the keys press will move them forward otherwise they will never stop
        player.x_vel = 0
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            hitLeft = game.collide(player, level.levelObjects, -PLAYER_VELOCITY * 2)
            if not hitLeft:
                player.moveLeft(PLAYER_VELOCITY)
        if keys[pygame.K_d]:
            hitRight = game.collide(player, level.levelObjects, PLAYER_VELOCITY * 2)
            if not hitRight:
                player.moveRight(PLAYER_VELOCITY)


        #STEP: Update Pos
        player.loop(FPS)
        level.loop()
        game.handleVerticalCollision(player, level.levelObjects, player.y_vel)
        objs = game.handleVerticalCollision(player, level.obsticals, player.y_vel)

        for obj in objs:
            if obj and obj.name == "fire":
                player.takeDamage()
            if obj and obj.name == "spike":
                player.takeDamage()


        #STEP: Draw Games
        game.draw(screen)

        level.draw(screen, offset_x)

        player.draw(screen,offset_x)
        pygame.display.update()

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel


    # STEP:Clear up 
    pygame.quit()
    sys.exit()
3

if __name__ == "__main__":
    main(screen)

