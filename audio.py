import config
import pygame as pg

pg.mixer.init()
pg.mixer.set_num_channels(20)

# metronome_sound = pg.mixer.Sound(config.METRONOME_SOUND_FILE)
beep_sound = pg.mixer.Sound(config.BEEP_SOUND_FILE)
boop_sound = pg.mixer.Sound(config.BOOP_SOUND_FILE)
miss_sound = pg.mixer.Sound(config.MISS_SOUND_FILE)

backtrack = pg.mixer.Sound(config.BACKTRACK_FILE)
p0_backtrack = pg.mixer.Sound(config.P0BACKTRACK_FILE)
p1_backtrack = pg.mixer.Sound(config.P1BACKTRACK_FILE)

chromatic_scale_list = []
for note in config.CHROMATIC_SCALE:
    chromatic_scale_list.append(pg.mixer.Sound(note))

score_reset_sound = pg.mixer.Sound(config.SCORE_RESET_SOUND_FILE)
fight_sound = pg.mixer.Sound(config.FIGHT_SOUND_FILE)
round_sounds = [pg.mixer.Sound(config.ROUND_SOUND_FILES[0]),pg.mixer.Sound(config.ROUND_SOUND_FILES[1]),pg.mixer.Sound(config.ROUND_SOUND_FILES[2])]
#finish_them_sound = pg.mixer.Sound(config.FINISH_THEM_SOUND_FILE)
generic_finisher = pg.mixer.Sound(config.GENERIC_FINISHER_EXPLOSION)


player0_voice = pg.mixer.Channel(0)
player1_voice = pg.mixer.Channel(1)
SFX = pg.mixer.Channel(2)
metronome = pg.mixer.Channel(3)
buzzer = pg.mixer.Channel(4)
background = pg.mixer.Channel(5)
narrator = pg.mixer.Channel(6)
chromatic_scale = pg.mixer.Channel(7)
background_p0 = pg.mixer.Channel(8)
background_p1 = pg.mixer.Channel(9)


player_voices = [player0_voice, player1_voice]
