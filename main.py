import pygame as pg
from settings import Settings
import assets.values.strings as st
import assets.values.booleans as bools
import assets.values.integers as num
from plugins.image_parser import ImageParser
import plugins.key_event_listener as k_listen

pg.init()

#Defaults
df = Settings(pg)

#Initialize game
screen = pg.display.set_mode(df.screen_size)
pg.display.set_caption(st.app_name)
pg.display.set_icon(df.set_ico)

#Start the game
while bools.playing:
    
    #Draw background and draw map
    df.set_background(screen)
    df.create_map(screen,pg)

    #Quit game
    for event in pg.event.get():
        if event.type is pg.QUIT:
            bools.playing = False
        
    #Mario movement plugin
    k_listen.key_press(pg, num, bools)
    
    #Animation plugin
    df.animate_char_mario(screen, pg)

    #Game mechanics plugin
    df.plugin_game_mechanics()

    pg.display.flip()
    pg.time.delay(num.fps)
            
    
