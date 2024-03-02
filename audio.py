import config
import pygame as pg

pg.mixer.init()

# metronome_sound = pg.mixer.Sound(config.METRONOME_SOUND_FILE)
beep_sound = pg.mixer.Sound(config.BEEP_SOUND_FILE)
boop_sound = pg.mixer.Sound(config.BOOP_SOUND_FILE)


player0_voice = pg.mixer.Channel(0)
player1_voice = pg.mixer.Channel(1)
SFX = pg.mixer.Channel(2)
metronome = pg.mixer.Channel(3)
buzzer = pg.mixer.Channel(4)
backtrack = pg.mixer.Channel(5)

player_voices = [player0_voice, player1_voice]
