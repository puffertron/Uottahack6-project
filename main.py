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

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # elif event.type == pg.KEYDOWN:
            #     if event.unicode == "a":
            #         print(time_since_beat)
            #         if (time_since_beat < config.perfect_time_tol) or ((time_since_beat-ms_per_beat) > -config.perfect_time_tol):
            #             print("You did PERFECT!!!!!!")
            #         elif (time_since_beat < config.great_time_tol) or ((time_since_beat-ms_per_beat) > -config.great_time_tol):
            #             print("Pretty Great!")
            #         else:
            #             print("nah, you missed")
        
        time_since_beat = pg.time.get_ticks() % ms_per_beat
        
        #when new input, check to see if at great time
        


        # TODO - get input

        # TODO - send input to Fight function

    
    






if __name__ == "__main__":
    main()