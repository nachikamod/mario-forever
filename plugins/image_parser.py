#Image parser method

static_img_dir = 'assets/images/static/'
mario_anim = 'assets/images/dynamic/'

map_ground = 'map/ground/'
obstacles = static_img_dir + 'map/obstacles/'
mario_anim = mario_anim + 'mario/'

class ImageParser():

    def __init__(self, pg):
        self.parse_icon = pg.image.load(static_img_dir +'logo.png')
        self.parse_ground = pg.image.load(static_img_dir + map_ground + 'level_1.png')

        self.parse_small_pipe = pg.image.load(obstacles + 'pipe_small.png')        
        
        self.mario_idle = pg.image.load(mario_anim + 'idle.png')

        self.mario_forward = [pg.image.load(mario_anim + 'forward_step_1.png'), pg.image.load(mario_anim + 'forward_step_2.png'), pg.image.load(mario_anim + 'forward_step_3.png'), pg.image.load(mario_anim + 'forward_step_4.png'), pg.image.load(mario_anim + 'forward_step_5.png')]
        self.mario_backward = [pg.image.load(mario_anim + 'backward_step_1.png'), pg.image.load(mario_anim + 'backward_step_2.png'), pg.image.load(mario_anim + 'backward_step_3.png'), pg.image.load(mario_anim + 'backward_step_4.png'), pg.image.load(mario_anim + 'backward_step_5.png')] 

