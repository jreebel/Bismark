from sprites import *
import pygame_gui
from os import path
import sys


def get_game_type(game):
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    start_list = pygame_gui.elements.ui_selection_list.UISelectionList(
        relative_rect=pg.Rect((350, 275), (100, 50)),
        item_list=['New', 'Load'],
        manager=manager)
    start_choice = False
    clock = pg.time.Clock()

    while not start_choice:
        # time_delta = clock.tick(60)/1000.0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print('quiting')
                game.quit()
            if event.type == pg.USEREVENT:
                if event.user_type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
                    start_choice = start_list.get_single_selection()
                    start_list.kill()
            manager.process_events(event)

        # manager.update(time_delta)
        game.screen.blit(game.background, (0, 0))
        manager.draw_ui(game.screen)
        pg.display.update()

    return start_choice


def initial_setup(game):
    if game.game_type == 'New':
        filename = path.join(game.file_dir, 'initial_setup.csv')
    else:
        filename = path.join(game.file_dir, 'old_file.csv')
        game.beep.play()

    unit_info = []
    infile = open(filename, 'r')
    for line in infile:
        unit_info = []
        if line[0] == '#' or line[0] == 'R':
            pass
        else:
            i = 0
            end = len(line)
            comma = line.find(',')
            substr = line
            while True:
                token = substr[0:comma].rstrip('\n')  # rstrip to keep out of final token
                unit_info.append(token)
                i += comma + 1
                if i >= end:
                    break
                else:
                    substr = substr[comma + 1:end]
                    comma = substr.find(',')
                    if comma < 0:
                        comma = end  # end of line generates -1
            create_unit(game, unit_info)
    infile.close()


def create_unit(game, info):
    if info[U_SEA_AIR] == 'S':
        game.ships.append(SeaUnit(game, info))
    elif info[U_SEA_AIR] == 'A':
        game.planes.append(AirUnit(game, info))
    else:
        game.beep.play()
        print('Bad unit type in input file!')
        game.quit()


def sea_movement(game, m, mx, my):
    if not game.current_ship:
        # Find the chosen ship
        i = 0
        while i < len(game.ships):
            s = game.ships[i]
            if mx >= s.rect.x and mx <= (s.rect.x + TILESIZE) \
                    and my >= s.rect.y and my <= (s.rect.y + TILESIZE):
                game.current_ship = s
                break
            i += 1
    else:
        if m[0] == 1:
            mouse_pos = vec(mx, my)
            if game.current_ship:
                limit = BASIC_MOVEMENT * game.current_ship.movement
                move = game.current_ship.ppos - mouse_pos
                if int(move.length()) > limit:
                    game.beep.play()
                else:
                    #  print(f'moving to {mx}, {my}')
                    game.current_ship.rect.centerx = mx
                    game.current_ship.rect.centery = my
                    game.current_ship.ppos = vec(mx, my)
                    game.current_ship.moved = True
