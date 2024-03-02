import pygame as pg
from setup import setup
import config


def main():

    pg.init()
    screen = pg.display.set_mode((config.windowWidth, config.windowHeight))
    # clock = pg.time.Clock()   - this is not actually used
    running = True
    setup()


    # Setting up some variables
    ms_per_beat = 60000 / config.bpm

    while running:

        time_since_last_beat = pg.time.get_ticks() % ms_per_beat

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # elif event.type == pg.KEYDOWN:
            #     if event.unicode == "a":
            #         print(time_since_last_beat)
        
        # TODO - get input

        # TODO - send input to Fight function

    
    






if __name__ == "__main__":
    main()