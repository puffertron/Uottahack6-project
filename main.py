import pygame as pg
from setup import setup
import config, padinput
import math


def main():

    pg.init()
    screen = pg.display.set_mode((config.windowWidth, config.windowHeight))
    clock = pg.time.Clock()   #- this is not actually used
    running = True
    setup()


    while running:

        time_since_last_beat = pg.time.get_ticks() % config.bpm

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN:
                if event.unicode == "a":
                    print(pg.time.get_ticks())
        
        screen.fill("purple")
        
        # TODO - get input
        pad1, pad2, = padinput.setupPads()
        pad1_raw_input, pad1_strings_input = padinput.getPadInput(pad1)
        pad2_raw_input, pad2_strings_input = padinput.getPadInput(pad2)
        padinput.drawPads(screen, (pad1_raw_input, pad2_raw_input))

        

        # TODO - send input to Fight function


        pg.display.flip()
        clock.tick(120)



if __name__ == "__main__":
    main()