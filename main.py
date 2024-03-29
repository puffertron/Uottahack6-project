import pygame as pg
from setup import setup
import config, padinput
import math
from fight import Fight
import audio
from state import State
import keyboard_input

def main():

    pg.init()
    screen = pg.display.set_mode((config.windowWidth, config.windowHeight))
    clock = pg.time.Clock()
    running = True
    setup()
    finisher_counter = 0
    finisher_sequence = []


    # Setting up some variables
    ms_per_beat = 60000 / config.BPM
    time_since_beat = 0 #Goes from 0 to ms_per_beat
    updated_this_beat = True #goes to false when time_since_beat resets, goes to true when Fight happens
    off_beat_played = True #goes to false when time_since_beat resets, goes to true when offBeat function happens happens
    stances:tuple[dict[str: list[str]], dict[str: list[str]]] = ({"perfect":[], "good":[], "held":[]}, {"perfect":[], "good":[], "held":[]})
    
    clock.tick()
    audio.background.play(audio.backtrack, loops=-1)
    audio.background_p0.play(audio.p0_backtrack, loops=-1)
    audio.background_p1.play(audio.p1_backtrack, loops=-1)
    Fight.roundStart()

    while running:
        
        # DEAL WITH EVENTS (keyboard and mouse)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.unicode == "a":
                    print(pg.time.get_ticks())

        # GET DDR INPUTS
        # Get newly pressed input (& what buttons were HELD TODO)
        #NOTE:Comment/Uncomment this line if you want to use pads
        """ pad0, pad1, = padinput.setupPads()
        pad0_raw_input, pad0_strings_input = padinput.getPadInput(pad0, 0)
        pad1_raw_input, pad1_strings_input = padinput.getPadInput(pad1, 1) 
        inputs = [pad0_strings_input, pad1_strings_input]"""
        player_0_data, player_1_data = keyboard_input.getKeyBoardInput()
        keyboard_p0_raw_input, keyboard_p0_strings_input = player_0_data
        keyboard_p1_raw_input, keyboard_p1_strings_input = player_1_data
        inputs = [keyboard_p0_strings_input, keyboard_p1_strings_input]
        

        #Finisher Helper
        double_input = []

        #When a winner has been decided
        if State.winner != 2:

            #TODO Restart the game
            if "start" in inputs[0] or "start" in inputs[1]:
                State.winner = 2
                finisher_sequence = []
                finisher_counter = 0
                State.player0_score = 0
                State.player1_score = 0
                #other things that need to be restart go here

            #When two inputs have been stored
            if len(double_input) > 1:
                double_input.sort()
                finisher_sequence.append(double_input)
                double_input = []

            
            #What happens when player 0 has won does and input
            elif State.winner == 0 and len(inputs[0]) > 0:
                #Make error noise when chromatic scale is done playing
                if(finisher_counter > 12):
                    #do error noise (doesn't exist yet, current is placeholder)
                    audio.buzzer.play(audio.miss_sound)
                    print()
                else:
                    double_input.append(inputs[0])
                    #play incrementing audio
                    audio.chromatic_scale.play(audio.chromatic_scale_list[finisher_counter % 12])
                    finisher_counter += 1
            
            #What happens when player 1 has won does and input
            elif State.winner == 1 and len(inputs[1]) > 0:
                if(finisher_counter > 12):
                    #do error noise (doesn't exist yet, current is placeholder)
                    audio.buzzer.play(audio.miss_sound)
                    print()
                else:
                    double_input.append(inputs[1])
                    #play incrementing audio
                    audio.chromatic_scale.play(audio.chromatic_scale_list[finisher_counter % 12])
                    finisher_counter += 1
            
            #TODO Determine what finisher sound to play
            #if finisher_sequence in config.FINISHER_SEQUENCES.values():
                #play specific audio
                #audio.config.FINISHER_SEQUENCES.get(finisher_sequence.key)
                #print()
            if finisher_counter == config.MAX_FINISHER:
                #Play explosion/generic finisher sfx
                audio.generic_finisher.play()
                finisher_counter += 1

        else:  
            # When new input, check to see if at great time
            # TODO - add ability for HELD stances
            if State.pause_for_beats == 0: # only acknowledge inputs if not paused
                for player in [0,1]:
                    playerInput = inputs[player]
                    if len(playerInput) != 0:
                        #print("Input received:", time_since_beat)
                        if (time_since_beat < (config.PERFECT_TIME_TOL+config.TIME_OFFSET)) or ((time_since_beat-ms_per_beat) > (-config.PERFECT_TIME_TOL+config.TIME_OFFSET)):
                            #print("You did PERFECT!!!!!!")
                            stances[player]["perfect"] += playerInput
                            Fight.onInput(playerInput, player)
                        elif (time_since_beat < config.GOOD_TIME_TOL+config.TIME_OFFSET) or ((time_since_beat-ms_per_beat) > (-config.GOOD_TIME_TOL+config.TIME_OFFSET)):
                            #print("Pretty Good!")
                            stances[player]["good"] += playerInput
                            Fight.onInput(playerInput, player)
                        else:
                            #print("nah, you missed")
                            audio.buzzer.play(audio.miss_sound)

            

            

            #print(time_since_beat)
            # DO THINGS AT SPECIFIC TIMES
            # bit after beat, Send input to fight function every beat        
            if (not updated_this_beat) and (time_since_beat > config.GOOD_TIME_TOL + config.TIME_OFFSET):
                # Only ever update after window where input is accepted
                updated_this_beat = True

                #print("before danceBattle time: ", time_since_beat)
                Fight.danceBattle(stances)
                #print("after danceBattle time: ", time_since_beat)
                print()
                #TODO - deal with return value and move it to proper place
                # if returnValue == True:
                #     print("danceBattle returned TRUE! Game is over, you got hit, whomp whomp")
                # elif returnValue == False:
                #     print("danceBattle returned FALSE, no one got hit, keep going!")
                # else:
                #     print("someone changed the return value of dance battle to a non boolean, programmers, fix me in main.py")
                # Clear stances
                stances:tuple[dict[str: list[str]], dict[str: list[str]]] = ({"perfect":[], "good":[], "held":[]}, {"perfect":[], "good":[], "held":[]})

            # on off-beat
            if (not off_beat_played) and (time_since_beat > (ms_per_beat/2)):
                Fight.onOffBeat()
                off_beat_played = True

            # on beat, play metronome
            if time_since_beat > ms_per_beat:
                time_since_beat -= ms_per_beat

                if State.pause_for_beats == 0: # pause_for_beats freezes game, stopping metronome and inputs
                    Fight.onBeat()
                elif State.pause_for_beats > 0:
                    State.pause_for_beats -= 1

                updated_this_beat = False
                off_beat_played = False
        


        #UPDATE VISUALS
        screen.fill("purple")

        #Keyboard variant
        padinput.drawPads(screen, (keyboard_p0_raw_input, keyboard_p1_raw_input), (keyboard_p0_strings_input, keyboard_p1_strings_input))
        #Pad variant
        #NOTE comment/uncomment this line if you want to use pads
        #padinput.drawPads(screen, (pad0_raw_input, pad1_raw_input), (pad0_strings_input, pad1_strings_input))

        pg.display.flip()
        time_since_beat += clock.tick(120)



if __name__ == "__main__":
    main()
