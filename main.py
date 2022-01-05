import pygame as pg
from random import randint

from rect import Player
from map import Map
from ball import Ball


def main(): 

    #Create variable clock, for tickrate for the game
    clock = pg.time.Clock()
    
    #Create the size of game display 
    screen = pg.display.set_mode((1024, 768))

    rect1 = Player(screen, 124, 300, pg.K_s, pg.K_w, (255, 0, 0))
    rect2 = Player(screen, 900, 300, pg.K_DOWN, pg.K_UP, (0, 0, 255))
    ball = Ball(screen, 512, 600)

    list_rect = pg.sprite.Group()
    list_rect.add(rect1)
    list_rect.add(rect2)

    #Create de Map
    mapa = Map()
    
    #Loop responsible for make the game runs infinitely
    game_loop = True

    #Principal loop
    while game_loop:
        clock.tick(30)

        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                game_loop = False


        rect1.move(mapa.wall_list)
        rect2.move(mapa.wall_list)
        ball.movimentation(mapa.wall_list, list_rect)

        screen.fill((40,40,40))

        mapa.wall_list.draw(screen)
        ball.drawn()
        rect1.drawn()
        rect2.drawn()

        pg.display.flip()


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()