import pygame as pg
from settings import *


def get_image(game, nationality, itype):
    if nationality == 'BR':
        if itype == 'CA':
            return game.br_ca_image.copy()
        elif itype == 'CL':
            return game.br_cl_image.copy()
        elif itype == 'CV':
            return game.br_cv_image.copy()
        elif itype == 'BB':
            return game.br_bb_image.copy()
        elif itype == 'BC':
            return game.br_bc_image.copy()
        elif itype == 'LR':
            return game.br_lr_image.copy()
        elif itype == 'FT':
            return game.br_ft_image.copy()
        elif itype == 'LB':
            return game.br_lb_image.copy()
        elif itype == 'TB':
            return game.br_tb_image.copy()
        elif itype == 'DB':
            return game.br_db_image.copy()
    elif nationality == 'GE':
        pass


class AirUnit(pg.sprite.Sprite):
    def __init__(self, game, info):
        if info[U_NATIONALITY] == 'BR':
            self.groups = game.all_sprites, game.br_air_sprites
        elif info[U_NATIONALITY] == 'GE':
            self.groups = game.all_sprites, game.ge_sea_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = info[U_NAME]
        self.image = get_image(game, info[U_NATIONALITY], info[U_TYPE])
        self.current = False
        self.moved = False
        self.movement = info[U_MOVEMENT]
        self.patrol_movement = info[U_PATROL_MOVEMENT]
        self.rect = self.image.get_rect()
        self.rect.centerx = int(info[U_STARTX])
        self.rect.centery = int(info[U_STARTY])
        self.start_turn = int(U_TURNAVAILABLE)  # zero means variable
        self.patrol_day_search = int(info[U_PDAYSEARCH])
        self.patrol_nite_search = int(info[U_PNITESEARCH])
        self.mvmt_day_search = int(info[U_DAYSEARCH])
        self.mvmt_nite_search = int(info[U_NITESEARCH])
        self.mode = info[U_MODE]
        self.basex = info[U_BASEX]
        self.basey = info[U_BASEY]
        self.endurance = info[U_ENDURANCE]
        self.patrol_endurance = info[U_PATROL_ENDURANCE]
        self.sea_air = info[U_SEA_AIR]
        # self.pos = vec(x, y)
        self.ppos = vec(self.rect.centerx, self.rect.centery)   # previous x y position


class SeaUnit(pg.sprite.Sprite):
    def __init__(self, game, info):
        if info[U_NATIONALITY] == 'BR':
            self.groups = game.all_sprites, game.br_sea_sprites
        elif info[U_NATIONALITY] == 'GE':
            self.groups = game.all_sprites, game.ge_sea_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = info[U_NAME]
        self.image = get_image(game, info[U_NATIONALITY], info[U_TYPE])
        self.current = False
        self.moved = False
        self.movement = float(info[U_MOVEMENT])
        self.rect = self.image.get_rect()
        self.rect.centerx = int(info[U_STARTX])
        self.rect.centery = int(info[U_STARTY])
        self.start_turn = int(U_TURNAVAILABLE)  # zero means variable
        self.patrol_day_search = int(info[U_PDAYSEARCH])
        self.patrol_nite_search = int(info[U_PNITESEARCH])
        self.mvmt_day_search = int(info[U_DAYSEARCH])
        self.mvmt_nite_search = int(info[U_NITESEARCH])
        self.task_force = info[U_TASKFORCE]
        self.convoy = info[U_CONVOY]
        self.mode = info[U_MODE]
        self.evasion_rating = int(info[U_EVASIVE])
        self.fuel = int(info[U_FUEL])
        self.sea_air = info[U_SEA_AIR]
        # self.pos = vec(x, y)
        self.ppos = vec(self.rect.centerx, self.rect.centery)   # previous x y position

    def update(self):
        pass

