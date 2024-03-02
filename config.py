# Holds config values so they are all in one place and easy to change


MAX_STANCE_MEMORY = 16

# Visual Settings
windowWidth = 500 #pxl?
windowHeight = 500 #pxl?

# Audio files
METRONOME_SOUND_FILE = "sounds/kick.wav"
MISS_SOUND_FILE = "sounds/womp.wav"
HIT_SOUND_FILE = "sounds/big_cymbal.wav"
PARRY_SOUND_FILE = "sounds/kick.wav"
FUMBLE_SOUND_FILE = "sounds/womp.wav"
ATTACK_SOUND_FILE = "sounds/tick.wav"
DODGE_SOUND_FILE = "sounds/metronome_off_beat.wav"
#FUMBLE_SOUND_FILE = ""

# Audio
BPM = 60 #1000ms per beat
GOOD_TIME_TOL = 150 #ms
PERFECT_TIME_TOL = 15 #ms
TIME_OFFSET = 20 #ms, positive number shifts all timing hit windows later (audio plays earlier)
