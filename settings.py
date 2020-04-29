from plugins.image_parser import ImageParser
from plugins.map.static_content import GenerateMap
from plugins.map.dynamic_content import GenerateChars
from plugins.map.game_mechanics import GameMechanics
import assets.values.integers as num
import assets.values.booleans as bools


class Settings():
    def __init__(self,pg):
        self.screen_size = num.screen_dimen
        
        #call image parser class
        im = ImageParser(pg)
        self.set_ico = im.parse_icon

    #Background color
    def set_background(self,screen):
        screen.fill(num.bg_color)

    #Sub plugin place ground and obstacle
    def create_map(self, screen, pg):
        im = ImageParser(pg)
        map_init = GenerateMap() 
        map_init.place_ground(screen, pg, im, num) 
        map_init.place_obstacles(screen, pg, im, num)

    #Sub plugin draw character mario
    def animate_char_mario(self, screen, pg):
        im = ImageParser(pg)
        mario_init = GenerateChars()
        mario_init.birth_mario(screen, pg, im, num, bools)

    #Sub plugin game mechanics
    def plugin_game_mechanics(self):
        mechanics_init = GameMechanics()
        mechanics_init.obstacle_mechanics(bools, num)
