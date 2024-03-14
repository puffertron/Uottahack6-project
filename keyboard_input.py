import pygame as pg
import math

PLAYER_0_INPUTS = [pg.K_q, pg.K_w, pg.K_e,
                   pg.K_a, pg.K_s, pg.K_d,
                   pg.K_z, pg.K_x, pg.K_c,
                   pg.K_1, pg.K_2]
PLAYER_1_INPUTS = [pg.K_t, pg.K_y, pg.K_u,
                   pg.K_g, pg.K_h, pg.K_j,
                   pg.K_b, pg.K_n, pg.K_m,
                   pg.K_6, pg.K_7]

INPUT_NAMES = [
        "nw",   "n", "ne",
        "w", "m", "e",
        "sw", "s", "se",
        "start", "select"
        ]

delta_inputs_0 = []
delta_inputs_1 = []

def getKeyBoardInput() -> tuple[tuple[list, list], tuple[list, list]]:
    global delta_inputs_0
    global delta_inputs_1

    #Get input data
    p0_raw_input, p0_strings_input, delta_inputs_0 = _getPlayerInput(0, delta_inputs_0)
    p1_raw_input, p1_strings_input, delta_inputs_1 = _getPlayerInput(1, delta_inputs_1)

    #return values
    player_0_input_data = (p0_raw_input, p0_strings_input)
    player_1_input_data = (p1_raw_input, p1_strings_input)

    return (player_0_input_data, player_1_input_data)

def _getPlayerInput(player_num, player_delta_inputs) -> tuple[list,list,list]:
    #Choose the input values to assess
    if player_num:
        input_vals = PLAYER_0_INPUTS
    else:
        input_vals = PLAYER_1_INPUTS

    #Get all pressed keys
    #TODO might want to move this line to getKeyBoardInput (just in case something weird happens)
    pressed = pg.key.get_pressed()

    #Generate bool values corresponding to inputs
    inputs = []
    for key in input_vals:
        if pressed[key]:
            inputs.append(True)
        else:
            inputs.append(False)

    """Copied from padinput"""

    input_strings = []
    just_pressed_input_strings= []
    #generate list of strings for just pressed buttons
    for i, input in enumerate(inputs):
        if input:
            #print("woot")
            input_strings.append(INPUT_NAMES[i]) 

    just_pressed_input_strings = list(input_strings)
    
    #filter held presses
    for press in input_strings:
        if press in player_delta_inputs:
            just_pressed_input_strings.remove(press)
    
    player_delta_inputs = input_strings

    return inputs, just_pressed_input_strings, player_delta_inputs

def drawPadInput(input, just_pressed):
    """Draws a representation of a pad on the screen."""
    padsurf = pg.surface.Surface((90,90)) # big surface for a 9 panel pad
    padsurf.fill((200,200,0))
    padrect = padsurf.get_rect()
    
    panels = []
    for i in range(0,9):
        if i != 4:
            p = pg.surface.Surface((30,30)) # small surface to represent 1 square
            p.fill((50*(i%2),50*(i%2),50*(i%2)))
            if input[i]: #turn white if pressed
                p.fill((255*(i%2),255,255))
            if INPUT_NAMES[i] in just_pressed: #flash red if step is just pressed
                p.fill((255,0,0))
            padsurf.blit(p, p.get_rect().move(math.floor(i/3)*30,(i%3)*30))

    return padsurf

def drawPads(screen, rawinputs, just_pressed):
    """Draws the debug pads"""
    screen.blit(pg.transform.flip(drawPadInput(rawinputs[0], just_pressed[0]),1,1), pg.Rect(50,50,90,90))
    screen.blit(drawPadInput(rawinputs[1], just_pressed[1]), pg.Rect(50+90+20,50,90,90))
