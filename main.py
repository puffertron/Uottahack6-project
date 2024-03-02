import pygame as pg
from setup import setup
import config
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

    while running:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # elif event.type == pg.KEYDOWN:
            #     if event.unicode == "a":
            #         print(time_since_beat)
            #         if (time_since_beat < config.perfect_time_tol) or ((time_since_beat-ms_per_beat) > -config.perfect_time_tol):
            #             print("You did PERFECT!!!!!!")
            #             TODO - add to list of perfects
            #         elif (time_since_beat < config.good_time_tol) or ((time_since_beat-ms_per_beat) > -config.good_time_tol):
            #             print("Pretty Good!")
            #         else:
            #             print("nah, you missed")
        
        # TODO - get input

        #when new input, check to see if at great time (code commented above when press 'a')

        # TODO - send input to Fight function
        todo = ({"test":[["",""],["",""]]},{"test":[["",""],["",""]]})

        time_since_beat += clock.tick()
        if (not updated_this_beat) and (time_since_beat > config.perfect_time_tol):
            # Only ever update after window where input is accepted
            updated_this_beat = True
            Fight.danceBattle(todo)
        
        if time_since_beat > ms_per_beat:
            time_since_beat -= ms_per_beat
            updated_this_beat = False
        

        # NO LONGER USED, CAN BE REMOVED
        # last_time_since_beat = time_since_beat
        # time_since_beat = pg.time.get_ticks() % ms_per_beat
        
        


        

    
    






if __name__ == "__main__":
    main()