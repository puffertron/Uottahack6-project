import pygame
import math

pygame.joystick.init()

input_names = [
        "nw", "n", "ne",
        "w", "m", "e",
        "sw", "s", "se"
        ]

#get any joysticks that are connected to the machine
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

delta_inputs_1 = []
delta_inputs_2 = []

#get the ddr pads, prolly should have some kind of verification sequence to make sure these r the pads
def setupPads(): 
    pad1 = joysticks[0]
    pad2 = joysticks[1]
    return pad1, pad2

cornerbuttons = [2,1,0,3] #bottomleft, topright, topleft, bottomright



def getPadInput(pad: pygame.joystick.Joystick, pad_number):
    global delta_inputs_1
    global delta_inputs_2

    if pad_number:
        delta_inputs = delta_inputs_2
    else:
        delta_inputs = delta_inputs_1

    axis1 = pad.get_axis(0)
    axis2 = pad.get_axis(1) 

    buttons=[]
    for i in cornerbuttons:
        buttons.append(pad.get_button(i))

    inputs = [ 
        buttons[1],                 axis2 < -0.5 or axis2 == 0, buttons[0], 
        axis1 > 0.5 or axis1 == 0, None,                   axis1 < -0.5 or axis1 == 0,
        buttons[3],                 axis2 > 0.5 or axis2 == 0,  buttons[2], 0, 0
        ]
    
    input_strings = []
    just_pressed_input_strings= []
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
        delta_inputs_2 = input_strings
    else:
        delta_inputs_1 = input_strings

    #print( "pad ", pad_number,just_pressed_input_strings, delta_inputs, input_strings, inputs)
    
    return inputs, just_pressed_input_strings

def drawPadInput(input, just_pressed):
    padsurf = pygame.surface.Surface((90,90))
    padsurf.fill((200,200,0))
    padrect = padsurf.get_rect()
    
    panels = []
    for i in range(0,9):
        if i != 4:
            p = pygame.surface.Surface((30,30))
            p.fill((50*(i%2),50*(i%2),50*(i%2)))
            if input[i]:
                p.fill((255*(i%2),255,255))
            if input_names[i] in just_pressed:
                p.fill((255,0,0))
            padsurf.blit(p, p.get_rect().move(math.floor(i/3)*30,(i%3)*30))


    return padsurf

def drawPads(screen, rawinputs, just_pressed):
    screen.blit(pygame.transform.flip(drawPadInput(rawinputs[0], just_pressed[0]),1,1), pygame.Rect(50,50,90,90))
    screen.blit(drawPadInput(rawinputs[1], just_pressed[1]), pygame.Rect(50+90+20,50,90,90))