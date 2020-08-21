import pygame as pg
from settings import *
from random import randint


def get_visibility(game):
    change_table = [1, 2, 3, 4, 5, 6, 0, -6, -5, -4, -3, -2, -1]
    if game.current_turn == 1:
        visibility = 4
    else:
        roll = randint(2, 12)
        if game.prev_visibility == 7:
            roll += 1
        elif game.prev_visibility == 8 or game.prev_visibility == 9:
            roll += 2

        if roll > 13:
            roll = 13

        visibility = game.prev_visibility + (change_table[roll - 1])  # zero based table offset
        if visibility > 9:
            visibility = 9
        elif visibility < 1:
            visibility = 1

    return visibility


def draw_text(game, text, font_name, size, color, x, y, align="nw"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if align == "nw":
        text_rect.topleft = (x, y)
    if align == "ne":
        text_rect.topright = (x, y)
    if align == "sw":
        text_rect.bottomleft = (x, y)
    if align == "se":
        text_rect.bottomright = (x, y)
    if align == "n":
        text_rect.midtop = (x, y)
    if align == "s":
        text_rect.midbottom = (x, y)
    if align == "e":
        text_rect.midright = (x, y)
    if align == "w":
        text_rect.midleft = (x, y)
    if align == "center":
        text_rect.center = (x, y)
    game.screen.blit(text_surface, text_rect)
