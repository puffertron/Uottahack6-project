import config
import pygame as pg

metronome_sound = pg.mixer.Sound(config.METRONOME_SOUND_FILE)
miss_sound = pg.mixer.Sound(config.MISS_SOUND_FILE)
aggressive_sound = pg.mixer.Sound(config.AGGRESSIVE_SOUND_FILE)
defensive_sound = pg.mixer.Sound(config.DEFENSIVE_SOUND_FILE)
hit = pg.mixer.Sound(config.HIT_SOUND_FILE)
parry = pg.mixer.Sound(config.PARRY_SOUND_FILE)
#fumble = pg.mixer.Sound(config.FUMBLE_SOUND_FILE)
