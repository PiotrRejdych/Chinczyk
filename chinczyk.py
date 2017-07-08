try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    import time
    from socket import *
    from pygame.locals import *
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)

def load_png(name):
    """ Load image and return image object"""
    fullname = name
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

def main():
    #Define constants
    global MENU
    global MENU_INITIALIZE
    global GAMEPLAY
    global GAMEPLAY_INITIALIZE
    MENU = 0
    MENU_INITIALIZE = 1
    GAMEPLAY = 2
    GAMEPLAY_INITIALIZE = 3
    size = width, height = 1000, 1005
    speed = [3, 3]
    BLACK = 0, 0, 0

    # Initialise screen
    pygame.init()
    pygame.display.set_caption('Chinczyk by Eredin')
    screen = pygame.display.set_mode(size)

    # Initialize modes (screens)
    global mode
    mode = MENU_INITIALIZE

    # Initialise clock
    clock = pygame.time.Clock()

    #Initialize assets
    ball = pygame.image.load("assets/ball.bmp")
    ballrect = ball.get_rect()

    pionek, pionekrect = load_png("assets/pionek.png")

    button = pygame.image.load("assets/button_new_game.bmp")
    buttonrect = button.get_rect()
    buttonrect = buttonrect.move(100,100)

    background = pygame.image.load("assets/plansza.bmp")
    backgroundrect = background.get_rect()

    while 1:
        clock.tick(60)

        if mode == MENU:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if buttonrect.collidepoint(position):
                        mode = GAMEPLAY_INITIALIZE

            screen.fill(BLACK)
            screen.blit(button, buttonrect)
            pygame.display.flip()

        elif mode == MENU_INITIALIZE:
            #do smth
            mode = MENU




        # GAMEPLAY mode _________________________________________________________________________________________________________________
        elif mode == GAMEPLAY:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    pionekrect = pionekrect.move(position[0] - pionekrect.left - pionekrect.width/2, position[1] - pionekrect.top - pionekrect.height/2)
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        mode = MENU


            screen.fill(BLACK)
            screen.blit(background, backgroundrect)
            screen.blit(pionek, pionekrect)
            pygame.display.flip()



        elif mode == GAMEPLAY_INITIALIZE:
            mode = GAMEPLAY

        else:
            print "Zla wartosc mode"
            sys.exit(2)



if __name__ == '__main__': main()