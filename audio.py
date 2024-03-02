import config
import pygame as pg

aggressive_sound = pg.mixer.Sound(AGGRESSIVE_SOUND_FILE)
defensive_sound = pg.mixer.Sound(DEFENSIVE_SOUND_FILE)
hit = pg.mixer.Sound(config.HIT_SOUND_FILE)
parry = pg.mixer.Sound(config.PARRY_SOUND_FILE)
#fumble = pg.mixer.Sound(config.FUMBLE_SOUND_FILE)
