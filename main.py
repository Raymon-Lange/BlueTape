import os,sys, random, math
import pygame
from os import listdir
from os.path import isfile, join
from game import Game
from titledLevel import Level
from player import Player
from item import Item
from font import Font

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("BlueTape")

BG_COLOR = (255,255,255)
WIDTH, HEIGHT = 800, 720
FPS = 80
PLAYER_VELOCITY = 4

level_0 = {
		'terrain': 'levels/levels/0/level_0__terrain.csv',
		'fruits': 'levels/levels/0/level_0__fruits.csv',
		'player': 'levels/levels/0/level_0__player.csv',
		'traps': 'levels/levels/0/level_0__traps.csv'}

level_1 = {
		'terrain': 'levels/levels/1/level_1_terrain.csv',
		'fruits': 'levels/levels/1/level_1_fruits.csv',
		'player': 'levels/levels/1/level_1_player.csv',
		'traps': 'levels/levels/1/level_1_traps.csv'}

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
    path = join("assets", "MainCharacters", "NinjaFrog")
    player.loadSprite(path, 32, 32, True)
    player.loop(FPS)

    level = Level(level_0, HEIGHT, WIDTH)

    path = join("assets", "Menu", "Text", "Text (White) (8x10).png")
    whiteFont = Font(path)

    time = 0
    counter = 0
    points = 0

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
            hitLeft = game.collide(player, level.terrain_sprites, -PLAYER_VELOCITY * 2)
            if not hitLeft:
                player.moveLeft(PLAYER_VELOCITY)
        if keys[pygame.K_d]:
            hitRight = game.collide(player, level.terrain_sprites, PLAYER_VELOCITY * 2)
            if not hitRight:
                player.moveRight(PLAYER_VELOCITY)

        #STEP: Update Pos
        player.loop(FPS)
        level.loop()
        objs = game.handleVerticalCollision(player, level.terrain_sprites, player.y_vel)

        #STEP: Evualted player state based on collison 
        # a player is on a wall if not landed,  is collided and Xvel != 0
        
        objs = game.handleVerticalCollision(player, level.trap_sprites, player.y_vel)

        for obj in objs:
            if obj and obj.name == "fire":
                player.takeDamage()
            if obj and obj.name == "spike":
                player.takeDamage()
            if obj and obj.name == "saw":
                player.takeDamage()
            if obj and obj.name == "platform":
                obj.off()
            if obj and obj.name == "trampoline":
                player.jump(13)
                obj.on()
            if obj and obj.name == "fan":
                player.isFly = True
                player.jump(4)
            if obj and obj.name == "Box1":
                if player.y_vel > 0:
                    actions = obj.hit()
                    level.trap_sprites.remove(obj)

                    for action in actions:
                        level.addEffect(action)
                else:
                    player.rect.bottom = obj.rect.top +5
                    player.landed()

        objs = game.handleVerticalCollision(player, level.fruit_sprites, 0)

        for obj in objs:
                action = Item(obj.rect.x, obj.rect.y, obj.width, obj.height, "Collected")
                points += obj.pointValue
                level.addEffect(action)
                level.fruit_sprites.remove(obj)
   

        
        #STEP: Draw Games
        game.draw(screen)

        level.draw(screen, offset_x)

        player.draw(screen,offset_x)


        counter +=1
        if counter == FPS:
            counter = 0
            time += 1

        text = str(int(time / 60)) + ":" + str("{:02d}".format(time % 60))

        whiteFont.draw(text,screen, 335, 16 , 0, 4)

        whiteFont.draw(str(points),screen, 675, 16, 0 , 3)

        pygame.display.update()

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

        if player.rect.y > (HEIGHT * 2):
            player.rect = pygame.Rect(50,50,50,50)
            offset_x = 0
            player.y_vel = 0


    # STEP:Clear up 
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main(screen)

