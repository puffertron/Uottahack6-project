import config
import pygame as pg

pg.mixer.init()

metronome_sound = pg.mixer.Sound(config.METRONOME_SOUND_FILE)
beep_sound = pg.mixer.Sound(config.BEEP_SOUND_FILE)
boop_sound = pg.mixer.Sound(config.BOOP_SOUND_FILE)
miss_sound = pg.mixer.Sound(config.MISS_SOUND_FILE)
attack_sound = pg.mixer.Sound(config.ATTACK_SOUND_FILE)
dodge_sound = pg.mixer.Sound(config.DODGE_SOUND_FILE)
hit_sound = pg.mixer.Sound(config.HIT_SOUND_FILE)
parry_sound = pg.mixer.Sound(config.PARRY_SOUND_FILE)
fumble_sound = pg.mixer.Sound(config.FUMBLE_SOUND_FILE)

metronome = pg.mixer.Channel(0)
ticker = pg.mixer.Channel(1)
buzzer = pg.mixer.Channel(2)
