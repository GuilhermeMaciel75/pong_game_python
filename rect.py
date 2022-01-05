import pygame as pg

'''
Win = Size of screen
x = position x
y = position y
down =  turn down
up = turn up
color = color of the rect
'''

class Player(pg.sprite.Sprite):

    def __init__(self, win, x, y, down, up, color) :
        super().__init__()

        #"system" Atributes
        self.win =  win
        self.x = x
        self.y = y

        #movimentation Atributes 
        self.down = down
        self.up = up

        #Car atributes
        self.velocity = 7
        self.color = color

    #Rect move 
    def move(self):

        key = pg.key.get_pressed()

        if key[self.down]:
            self.y -= self.velocity 

        elif key[self.up]:
            self.y += self.velocity


    def drawn(self):
        
        pg.draw.rect(self.win, self.color, ((self.x, self.y),(15, 135)))
