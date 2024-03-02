import pygame

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

def get_pad_input(pad: pygame.joystick.Joystick):
    axis1 = pad.get_axis(0)
    axis2 = pad.get_axis(1)

    buttons=[]
    for i in cornerbuttons:
        buttons.append(pad.get_button(i))

    inputs = {"forward":max(axis1, 0), "back":min(axis1, 0), "left":max(axis2, 0), "right":max(axis2, 0), 
              "cross":buttons[0], "circle":buttons[1], "triangle":buttons[2], "square":buttons[3], "start":0, "select":0}
    return inputs

def draw_pad_input(input, color):
    padsurf = pygame.surface.Surface((90,90))
    padrect = padsurf.get_rect()
    


while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    print(get_pad_input(pad1))
    print(get_pad_input(pad2))

    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()