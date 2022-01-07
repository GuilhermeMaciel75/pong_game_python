import pygame as pg
from rect import Player

def show_pontuation(rect1, rect2, screen):

    font = pg.font.Font('assets/pong.ttf', 32)
    score_rect1 = font.render(f'{rect2.get_score}', True, (255, 255 ,255))
    score_rect2 = font.render(f'{rect1.get_score}', True, (255, 255 ,255))

    screen.blit(score_rect1, (424, 80))
    screen.blit(score_rect2, (600, 80))