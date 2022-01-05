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

        self.image = pg.Surface([15, 135])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    
        #movimentation Atributes 
        self.down = down
        self.up = up

        #Car atributes
        self.velocity = 7
        self.color = color

    #Rect move 
    def move(self, list_wall):

        key = pg.key.get_pressed()

        if key[self.down]:
            self.rect.y += self.velocity 

            list_colision = pg.sprite.spritecollide(self, list_wall, False)
            for colision in list_colision:
                self.rect.bottom = colision.rect.top


        elif key[self.up]:
            self.rect.y -= self.velocity
            
            list_colision = pg.sprite.spritecollide(self, list_wall, False)
            for colision in list_colision:
                self.rect.top = colision.rect.bottom


    def drawn(self):
        
        pg.draw.rect(self.win, self.color, self)
