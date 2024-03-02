import pygame as pg
from setup import setup
import config, padinput
import math
from fight import Fight


def main():

    pg.init()
    screen = pg.display.set_mode((config.windowWidth, config.windowHeight))
    clock = pg.time.Clock()
    running = True
    setup()


    # Setting up some variables
    ms_per_beat = 60000 / config.bpm
    time_since_beat = 0 #Goes from 0 to ms_per_beat
    updated_this_beat = True #goes to false when time_since_beat resets, goes to true when Fight happens
    stances:tuple[dict[str: list[str]], dict[str: list[str]]] = ({"perfect":[], "good":[], "held":[]}, {"perfect":[], "good":[], "held":[]})
        

    while running:
        
        # DEAL WITH EVENTS (keyboard and mouse)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.unicode == "a":
                    print(pg.time.get_ticks())
            # elif event.type == pg.KEYDOWN:
            #     if event.unicode == "a":
            #         print(time_since_beat)

        # GET DDR INPUTS
        # Get newly pressed input (& what buttons were HELD TODO)
        pad0, pad1, = padinput.setupPads()
        pad0_raw_input, pad0_strings_input = padinput.getPadInput(pad0, 0)
        pad1_raw_input, pad1_strings_input = padinput.getPadInput(pad1, 1)
        inputs = [pad0_strings_input, pad1_strings_input]

        # When new input, check to see if at great time
        # TODO - add ability for HELD stances
        for player in [0,1]:
            playerInput = inputs[player]
            if len(playerInput) != 0:
                if (time_since_beat < config.perfect_time_tol) or ((time_since_beat-ms_per_beat) > -config.perfect_time_tol):
                    print("You did PERFECT!!!!!!")
                    stances[player]["perfect"] += playerInput
                elif (time_since_beat < config.good_time_tol) or ((time_since_beat-ms_per_beat) > -config.good_time_tol):
                    print("Pretty Good!")
                    stances[player]["good"] += playerInput
                else:
                    print("nah, you missed")
                    #Make womp womp sound

        

        


        # Send input to fight function every beat        
        if (not updated_this_beat) and (time_since_beat > config.perfect_time_tol):
            # Only ever update after window where input is accepted
            updated_this_beat = True
            Fight.danceBattle(stances)
            # Clear stances
            stances:tuple[dict[str: list[str]], dict[str: list[str]]] = ({"perfect":[], "good":[], "held":[]}, {"perfect":[], "good":[], "held":[]})

        
        if time_since_beat > ms_per_beat:
            time_since_beat -= ms_per_beat
            updated_this_beat = False
        

        # NO LONGER USED, CAN BE REMOVED
        # last_time_since_beat = time_since_beat
        # time_since_beat = pg.time.get_ticks() % ms_per_beat
        

        #Update Visuals
        screen.fill("purple")

        padinput.drawPads(screen, (pad0_raw_input, pad1_raw_input), (pad0_strings_input, pad1_strings_input))

        pg.display.flip()
        time_since_beat += clock.tick(120)



if __name__ == "__main__":
    main()