import config
import pygame as pg

pg.mixer.init()

metronome_sound = pg.mixer.Sound(config.METRONOME_SOUND_FILE)
beep_sound = pg.mixer.Sound(config.BEEP_SOUND_FILE)
boop_sound = pg.mixer.Sound(config.BOOP_SOUND_FILE)
miss_sound = pg.mixer.Sound(config.MISS_SOUND_FILE)
aggressive_sound = pg.mixer.Sound(config.AGGRESSIVE_SOUND_FILE)
defensive_sound = pg.mixer.Sound(config.DEFENSIVE_SOUND_FILE)
hit_sound = pg.mixer.Sound(config.HIT_SOUND_FILE)
parry_sound = pg.mixer.Sound(config.PARRY_SOUND_FILE)
#fumble = pg.mixer.Sound(config.FUMBLE_SOUND_FILE)

ticker = pg.mixer.Channel(0)
