# Holds config values so they are all in one place and easy to change


MAX_STANCE_MEMORY = 16

# Visual Settings
windowWidth = 500 #pxl?
windowHeight = 500 #pxl?

# Audio files
BEEP_SOUND_FILE = "sounds/beep.wav" # metronome sounds
BOOP_SOUND_FILE = "sounds/boop.wav"
METRONOME_SOUND_FILE = "sounds/womp.wav"
METRONOME_SOUND_FILE = "sounds/kick.wav"
MISS_SOUND_FILE = "sounds/buzzer.wav"

# Specific to players
P0NOTE_FILE = "sounds/kick.wav"
P1NOTE_FILE = "sounds/kick.wav"
P0CHORD_FILE = "sounds/hithigh.wav"
P1CHORD_FILE = "sounds/hitlow.wav"
P0HIT_SOUND_FILE = "sounds/short_cymbals.wav"
P1HIT_SOUND_FILE = "sounds/short_cymbals.wav"
P0PARRY_SOUND_FILE = "sounds/clink.wav"
P1PARRY_SOUND_FILE = "sounds/clink.wav"
P0FUMBLE_SOUND_FILE = "sounds/womp.wav"
P1FUMBLE_SOUND_FILE = "sounds/womp.wav"
# ATTACK_SOUND_FILE = "sounds/kick.wav"
P0DODGE_SOUND_FILE = "sounds/kick.wav"
P1DODGE_SOUND_FILE = "sounds/kick.wav"

# Narrator sounds (players += 1)
P0ADVANTAGE_SOUND_FILE = "sounds/voicelines/advp1"
P1ADVANTAGE_SOUND_FILE = "sounds/voicelines/advp2"
P0WIN_SOUND_FILE = "sounds/voicelines/player1win"
P1WIN_SOUND_FILE = "sounds/voicelines/player2win"

BACKTRACK_FILE = "sounds/backing_loop.wav"


# Audio
BPM = 120 #1000ms per beat
GOOD_TIME_TOL = 150 #ms
PERFECT_TIME_TOL = 15 #ms
TIME_OFFSET = 20 #ms, positive number shifts all timing hit windows later (audio plays earlier)
