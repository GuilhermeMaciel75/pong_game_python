import pygame as pg

class Ball(pg.sprite.Sprite):
    def __init__(self, win, x, y):
        super().__init__()

        self.image = pg.Surface([15, 15])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.win = win

        self.velocity_x = 1
        self.velocity_y = 1

 
    def set_velocity_x(self, value):
        self.velocity_x = value

    def set_velocity_y(self, value):
        self.velocity_y = value

    def movimentation(self, list_wall, list_rect):

        self.rect.y -= self.velocity_y
        self.rect.x -= self.velocity_x

        if (pg.sprite.spritecollide(self, list_wall, False) or pg.sprite.spritecollide(self, list_rect, False)):

            if self.rect.top <= 48 or self.rect.bottom >= 720:
                self.velocity_y *= -1

        
            elif self.rect.left <= 63 or self.rect.right >= 1024: 
                self.velocity_x *= -1

            elif pg.sprite.spritecollide(self, list_rect, False):
                pass


        elif self.rect.left <= 64 and 576 >= self.rect.top >= 256:
            
            return 'rect1'
        
        elif self.rect.right >= 1024 and 576 >= self.rect.top >= 344:

            return 'rect2'

        return False

    def drawn(self):
        
        pg.draw.rect(self.win, (255, 255, 255), self)
