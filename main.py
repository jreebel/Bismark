import sys
from os import path
from maps import *
from phases import *
from functions import *
import pygame_gui


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # self.background = pg.Surface((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.current_ship = None
        self.game_type = None
        self.visibility = None
        self.load_data()
        self.map = TiledMap(path.join(self.img_dir, 'Test3.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.screen.blit(self.map_img, self.map_rect)
        pg.display.flip()
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.background.blit(self.map_img, self.map_rect)

    def load_data(self):
        self.img_dir = path.join(path.dirname(__file__), 'img')
        self.file_dir = path.join(path.dirname(__file__), 'files')
        self.snd_dir = path.join(path.dirname(__file__), 'snd')
        self.br_ca_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_CA.png')).convert_alpha()
        self.br_cl_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_CL.png')).convert_alpha()
        self.br_cv_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_CV.png')).convert_alpha()
        self.br_bb_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_BB.png')).convert_alpha()
        self.br_bc_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_BC.png')).convert_alpha()
        self.br_lr_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_LR.png')).convert_alpha()
        self.br_lr_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_LB.png')).convert_alpha()
        self.br_lb_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_LR.png')).convert_alpha()
        self.br_tb_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_TB.png')).convert_alpha()
        self.br_db_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_DB.png')).convert_alpha()
        self.br_ft_image = pg.image.load(path.join(self.img_dir, 'Bismark_BR_FT.png')).convert_alpha()
        self.beep = pg.mixer.Sound(path.join(self.snd_dir, 'blip.wav'))
        self.beep.set_volume(0.3)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.current_phase = 'Unit Availability'
        self.current_turn = 1
        # self.map = TiledMap(path.join(self.img_dir, 'Test3.tmx'))
        # self.map_img = self.map.make_map()
        # self.map_rect = self.map_img.get_rect()
        self.all_sprites = pg.sprite.Group()
        self.br_sea_sprites = pg.sprite.Group()
        self.ge_sea_sprites = pg.sprite.Group()
        self.br_air_sprites = pg.sprite.Group()
        self.ge_air_sprites = pg.sprite.Group()
        self.ships = []
        self.planes = []
        # if self.game_type:
        #     initial_setup(self)
        # self.screen.blit(self.map_img, self.map_rect)
        # pg.display.flip()
        # self.background = pg.Surface((WIDTH, HEIGHT))
        # self.background.blit(self.map_img, self.map_rect)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

            if self.current_phase == 'Unit Availability':
                if self.current_turn > 1:
                    pass
                self.current_phase = 'Determine Visibility'
            elif self.current_phase == 'Determine Visibility':
                self.visibility = get_visibility(self)
                self.current_phase = 'Task Forces and Convoys'
            # Determine visibility for turn

            # Task forces and convoys

            # Shadow determination

            # Air movement

            # sea_movement(self)

            # Search

            # Air attack

            # Chance

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        #  self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.map_rect)
        draw_text(self, 'Turn:  ' + str(self.current_turn), None, 24, BLACK, 677, 5, 'nw')
        draw_text(self, 'Phase:  ' + str(self.current_phase), None, 24, BLACK, 677, 20, 'nw')
        draw_text(self, 'Visibility:  ' + str(self.visibility), None, 24, BLACK, 677, 35, 'nw')
        self.all_sprites.draw(self.screen)
        if self.current_ship:
            if self.current_ship.moved:
                self.current_ship = None
            else:
                pg.draw.circle(self.screen, WHITE, (self.current_ship.rect.centerx,
                                                    self.current_ship.rect.centery),
                               int(self.current_ship.movement * TILESIZE), 1)
        pg.display.flip()

    def process_mouse_event(self, m, mx, my):
        if self.current_phase == 'sea_movement':
            sea_movement(self, m, mx, my)
        # if m[0] == 1:
        #     mouse_pos = vec(mx, my)
        #     if self.current_ship:
        #         limit = BASIC_MOVEMENT * CRUISER_MOVEMENT_ADJ
        #         move = self.current_ship.ppos - mouse_pos
        #         if int(move.length()) > limit:
        #             self.s.play()
        #         else:
        #             self.current_ship.rect.centerx = mx
        #             self.current_ship.rect.centery = my
        #             self.current_ship.ppos = vec(mx, my)
        #             self.current_ship.moved = True
        #     else:
        #         self.current_ship = self.norfolk

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                m = pg.mouse.get_pressed()
                mx, my = pg.mouse.get_pos()
                self.process_mouse_event(m, mx, my)


# create the game object
g = Game()
pg.mouse.set_cursor(*pg.cursors.broken_x)
pg.font.init()
while True:
    g.game_type = get_game_type(g)
    if g.game_type == 'New':
        g.new()
        initial_setup(g)
    else:
        pass  # g.old
    g.run()
