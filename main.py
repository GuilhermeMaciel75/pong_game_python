import pygame as pg
from random import randint

from rect import Player
from map import Map
from ball import Ball
from pontuation import show_pontuation


def main(): 

    #Create variable clock, for tickrate for the game
    clock = pg.time.Clock()
    
    #Create the size of game display 
    screen = pg.display.set_mode((1088, 768))

    rect1 = Player(screen, 124, 300, pg.K_s, pg.K_w, (255, 0, 0))
    rect2 = Player(screen, 900, 300, pg.K_DOWN, pg.K_UP, (0, 0, 255))

    list_rect = pg.sprite.Group()
    list_rect.add(rect1)
    list_rect.add(rect2)

    #Create de Map
    mapa = Map()
    
    

    #Principal loop
    while (rect1.get_score < 10) and (rect2.get_score < 10):
        
        game_loop = True
        clock.tick(30)
        ball = Ball(screen, 512, randint(20, 700))

        while True:
            
            for event in pg.event.get():
                
                if event.type == pg.QUIT:
                    rect1.set_score = 10
                    game_loop = False
                    break


            rect1.move(mapa.wall_list)
            rect2.move(mapa.wall_list)
            result = ball.movimentation(mapa.wall_list, list_rect)


            if result != False:
                if result == 'rect1':
                    rect1.set_score = 1

                elif result == 'rect2':
                    rect2.set_score = 1

                break
            

            screen.fill((40,40,40))

            show_pontuation(rect1, rect2, screen)

            mapa.wall_list.draw(screen)
            mapa.wall_list_no_colision.draw(screen)
            ball.drawn()
            rect1.drawn()
            rect2.drawn()

            pg.display.flip()


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()