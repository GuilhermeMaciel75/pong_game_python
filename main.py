import pygame as pg

from rect import Player
from map import Map


def main(): 

    #Create variable clock, for tickrate for the game
    clock = pg.time.Clock()
    
    screen = pg.display.set_mode((1024, 768))

    rect1 = Player(screen, 124, 300, pg.K_s, pg.K_w, (255, 0, 0))
    rect2 = Player(screen, 900, 300, pg.K_DOWN, pg.K_UP, (0, 0, 255))

    mapa = Map()
    
    game_loop = True
    while game_loop:
        clock.tick(30)

        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                game_loop = False


        rect1.move()
        rect2.move()

        screen.fill((40,40,40))

        mapa.wall_list.draw(screen)
        rect1.drawn()
        rect2.drawn()

        pg.display.flip()



if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()