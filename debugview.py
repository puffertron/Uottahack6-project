import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

pad1 = joysticks[0]
pad2 = joysticks[1]
cornerbuttons = [2,1,0,3] #bottomleft, topright, topleft, bottomright

def getPadInput(pad: pygame.joystick.Joystick):
    axis1 = pad.get_axis(0)
    axis2 = pad.get_axis(1) 

    buttons=[]
    for i in cornerbuttons:
        buttons.append(pad.get_button(i))

    input_names = [
        "nw", "n", "ne",
        "w", "m", "e",
        "sw", "s", "se"
        ]

    inputs = [
        buttons[1],                 axis2 < -0.5 or axis2 == 0, buttons[0], 
        axis1 > 0.5 or axis1 == 0, None,                   axis1 < -0.5 or axis1 == 0,
        buttons[3],                 axis2 > 0.5 or axis2 == 0,  buttons[2], 0, 0
        ]

    
    input_strings = []
    for i, input in enumerate(inputs):
        if input:
            input_strings.append(input_names[i])
    
    return inputs, input_strings

def drawPadInput(input):
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
            padsurf.blit(p, p.get_rect().move(math.floor(i/3)*30,(i%3)*30))


    return padsurf
        
def drawPads(screen, pads):
    i1, s1 =getPadInput(pads[0])
    i2, s2 = getPadInput(pads[1])
    screen.blit(pygame.transform.flip(drawPadInput(i1),1,1), pygame.Rect(50,50,90,90))
    screen.blit(drawPadInput(i2), pygame.Rect(50+90+20,50,90,90))
    #print(s1)

while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    
    i1, s1 =getPadInput(pad1)
    i2, s2 = getPadInput(pad2)
    screen.blit(pygame.transform.flip(drawPadInput(i1),1,1), pygame.Rect(50,50,90,90))
    screen.blit(drawPadInput(i2), pygame.Rect(50+90+20,50,90,90))
    print(s1)


    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()