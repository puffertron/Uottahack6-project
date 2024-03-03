# Holds config values so they are all in one place and easy to change


MAX_STANCE_MEMORY = 16
MAX_FINISHER = 12
FINISHER_SEQUENCES = { "Ciaran" : ["n", "s", "e" "w", "nw", "se", "ne", "sw", "nw", "se", "w", "e"]\
                      }

# Visual Settings
windowWidth = 500 #pxl?
windowHeight = 500 #pxl?

# Audio files
BEEP_SOUND_FILE = "sounds/beep.wav" # metronome sounds
BOOP_SOUND_FILE = "sounds/boop.wav"
METRONOME_SOUND_FILE = "sounds/womp.wav"
METRONOME_SOUND_FILE = "sounds/kick.wav"
MISS_SOUND_FILE = "sounds/buzzer.wav"

# Secific to players p0 is synth, p1 is drum
P0NOTE_FILE0 = "sounds/synthnote0.wav"
P0NOTE_FILE1 = "sounds/synthnote1.wav"
P0NOTE_FILE2 = "sounds/synthnote2.wav"
P0NOTE_FILE3 = "sounds/synthnote3.wav"
P1NOTE_FILE = "sounds/tambohit.wav"
P0CHORD_FILE = "sounds/hithigh.wav"
P1CHORD_FILE = "sounds/hithigh.wav"
P0HIT_SOUND_FILE = "sounds/big_cymbal.wav"
P1HIT_SOUND_FILE = "sounds/big_cymbal.wav"
P0OFFBEAT_SOUND_FILE = "sounds/lilbeep.wav"
P1OFFBEAT_SOUND_FILE = "sounds/ting.wav"
P0PARRY_SOUND_FILE = "sounds/clink.wav"
P1PARRY_SOUND_FILE = "sounds/clink.wav"
P0FUMBLE_SOUND_FILE = "sounds/womp.wav"
P1FUMBLE_SOUND_FILE = "sounds/womp.wav"
# ATTACK_SOUND_FILE = "sounds/kick.wav"
P0DODGE_SOUND_FILE = "sounds/woosh.wav"
P1DODGE_SOUND_FILE = "sounds/woosh.wav"

# Narrator sounds (players += 1)
P0ADVANTAGE_SOUND_FILE = "sounds/voicelines/advp1.wav"
P1ADVANTAGE_SOUND_FILE = "sounds/voicelines/advp2.wav"
P0WIN_SOUND_FILE = "sounds/voicelines/player1win.wav"
P1WIN_SOUND_FILE = "sounds/voicelines/player2win.wav"
SCORE_RESET_SOUND_FILE = "sounds/voicelines/scorereset.wav"
FIGHT_SOUND_FILE = "sounds/voicelines/fight.wav"

ROUND_SOUND_FILES = ["sounds/voicelines/round1.wav","sounds/voicelines/round2.wav","sounds/voicelines/finalround.wav"]

FINISH_THEM_SOUND_FILE = "sounds/voicelines/TODO" #TODO

BACKTRACK_FILE = "sounds/backing_loop.wav"


# Audio
BPM = 120 #1000ms per beat
GOOD_TIME_TOL = 150 #ms
PERFECT_TIME_TOL = 15 #ms
TIME_OFFSET = 20 #ms, positive number shifts all timing hit windows later (audio plays earlier)
