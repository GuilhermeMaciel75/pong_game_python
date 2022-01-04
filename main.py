import pygame as pg


def main(): 

    #Create variable clock, for tickrate for the game
    clock = pg.time.Clock()
    
    screen = pg.display.set_mode((1024, 768))
    screen.color('blue')



if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    exit()