import config
import pygame as pg

pg.mixer.init()

# metronome_sound = pg.mixer.Sound(config.METRONOME_SOUND_FILE)
beep_sound = pg.mixer.Sound(config.BEEP_SOUND_FILE)
boop_sound = pg.mixer.Sound(config.BOOP_SOUND_FILE)


metronome = pg.mixer.Channel(0)
ticker = pg.mixer.Channel(1)
buzzer = pg.mixer.Channel(2)




