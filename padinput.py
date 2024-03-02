import pg as pg
import math

pg.joystick.init()

#the input names for each button!
input_names = [
        "nw", "n", "ne",
        "w", "m", "e",
        "sw", "s", "se"
        ]

#get any joysticks that are connected to the machine
joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]

delta_inputs_0 = []
delta_inputs_1 = []

#get the ddr pads, prolly should have some kind of verification sequence to make sure these r the pads

def setupPads() -> tuple[pg.joystick.Joystick, pg.joystick.Joystick]:
    """Setup dance pad controllers. Returns two pg Joystick objects"""
    pad0 = joysticks[0]
    pad1 = joysticks[1]
    return pad0, pad1

cornerbuttons = [2,1,0,3] #bottomleft, topright, topleft, bottomright



def getPadInput(pad: pg.joystick.Joystick, pad_number) -> tuple[list, list]:
    """get input for a dance pad. returns raw input (List of int/bool) and inputs pressed this tick (list of strings)"""
    global delta_inputs_0
    global delta_inputs_1

    if pad_number:
        delta_inputs = delta_inputs_1
    else:
        delta_inputs = delta_inputs_0

    axis1 = pad.get_axis(0)
    axis2 = pad.get_axis(1) 

    buttons=[]
    for i in cornerbuttons:
        buttons.append(pad.get_button(i))

    #list of raw inputs, in int/bool form
    inputs = [ 
        buttons[1],                 axis2 < -0.5 or axis2 == 0, buttons[0], 
        axis1 > 0.5 or axis1 == 0, None,                   axis1 < -0.5 or axis1 == 0,
        buttons[3],                 axis2 > 0.5 or axis2 == 0,  buttons[2], 0, 0
        ]
    
    input_strings = []
    just_pressed_input_strings= []
    #generate list of strings for just pressed buttons
    for i, input in enumerate(inputs):
        if input:
            #print("woot")
            input_strings.append(input_names[i]) 

    just_pressed_input_strings = list(input_strings)
    
    #filter held presses
    for press in input_strings:
        if press in delta_inputs:
            just_pressed_input_strings.remove(press)
    
    delta_inputs = input_strings
    if pad_number:
        delta_inputs_1 = input_strings
    else:
        delta_inputs_0 = input_strings

    #print( "pad ", pad_number,just_pressed_input_strings, delta_inputs, input_strings, inputs)
    
    return inputs, just_pressed_input_strings

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
            if input_names[i] in just_pressed: #flash red if step is just pressed
                p.fill((255,0,0))
            padsurf.blit(p, p.get_rect().move(math.floor(i/3)*30,(i%3)*30))


    return padsurf

def drawPads(screen, rawinputs, just_pressed):
    """Draws the debug pads"""
    screen.blit(pg.transform.flip(drawPadInput(rawinputs[0], just_pressed[0]),1,1), pg.Rect(50,50,90,90))
    screen.blit(drawPadInput(rawinputs[1], just_pressed[1]), pg.Rect(50+90+20,50,90,90))