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

        self.velocity_x = 2
        self.velocity_y= 2

    def movimentation(self, list_wall, list_rect):



        self.rect.y += self.velocity_y
        self.rect.x += self.velocity_x
        """
        if  self.rect.y <= 720 and (pg.sprite.spritecollide(self, list_wall, False) or pg.sprite.spritecollide(self, list_rect, False)):
            self.velocity_y = self.velocity_y * -1
            self.rect.y += 2 * self.velocity_y

        elif self.rect.x <= 512 and (pg.sprite.spritecollide(self, list_wall, False) or pg.sprite.spritecollide(self, list_rect, False)):
            self.velocity_x = self.velocity_x * -1
            self.rect.x += self.velocity_x


        elif self.rect.x >= 512 and (pg.sprite.spritecollide(self, list_wall, False) or pg.sprite.spritecollide(self, list_rect, False)):
            self.velocity_x = self.velocity_x * -1
            self.rect.x += self.velocity_x
        """
        





        '''if self.rect.x  >= 512 and self.rect  and (pg.sprite.spritecollide(self, list_wall, False) or pg.sprite.spritecollide(self, list_rect, False)):
            
            self.velocity_y = self.velocity_y * -1
            self.rect.y += self.velocity_y
            
        elif self.rect.x  >= 512 and self.rect.y <= 384 and (pg.sprite.spritecollide(self, list_wall, False) or pg.sprite.spritecollide(self, list_rect, False)):
            self.velocity_x = self.velocity_x * -1
            self.rect.x += self.velocity_x

        elif self.rect.x  <= 512 and self.rect.y >= 384 and (pg.sprite.spritecollide(self, list_wall, False) or pg.sprite.spritecollide(self, list_rect, False)):
            self.velocity_y = self.velocity_y * -1
            self.rect.y += self.velocity_y

        elif self.rect.x  <= 512 and self.rect.y <= 384 and (pg.sprite.spritecollide(self, list_wall, False) or pg.sprite.spritecollide(self, list_rect, False)):
            self.velocity_y = self.velocity_y * -1
            self.rect.y += self.velocity_y'''


    def drawn(self):
        
        pg.draw.rect(self.win, (255, 255, 255), self)
