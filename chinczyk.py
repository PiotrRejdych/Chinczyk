try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    import time
    import load
    import Pionek
    import Plansza
    import Gracz
    from socket import *
    from pygame.locals import *
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)


def main():
    #Define constants
    global MENU
    global MENU_NEWGAME
    global GAMEPLAY
    global GAMEPLAY_INITIALIZE
    MENU = 0
    MENU_NEWGAME = 1
    GAMEPLAY = 3
    GAMEPLAY_INITIALIZE = 3
    SIZE = width, height = 1000, 1000
    BLACK = 0, 0, 0

    # Initialise screen
    pygame.init()
    pygame.display.set_caption('Chinczyk by Piotr Rejdych')
    screen = pygame.display.set_mode(SIZE)

    # Initialize modes (screens)
    global mode
    mode = MENU

    # Initialise clock
    clock = pygame.time.Clock()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Initialize assets
    ball = pygame.image.load("assets/ball.bmp")
    ballrect = ball.get_rect()

    global plansza
    plansza = Plansza.Plansza()

    global grupaGraczy
    global gracz
    gracz = Gracz.Gracz(grupaGraczy,)
    global pionek
    pionek = Pionek.Pionek((0, 0), Pionek.Pionek.CZERWONY)

    # Initialize menu assets
    naglowek = pygame.image.load("assets/naglowek.bmp")
    naglowek_rect = naglowek.get_rect()
    naglowek_rect = naglowek_rect.move(SIZE[0] / 2 - naglowek_rect.width / 2, 50)
    button_newgame = pygame.image.load("assets/button_new_game.bmp")
    button_newgame_rect = button_newgame.get_rect()
    button_newgame_rect = button_newgame_rect.move(SIZE[0]/2-button_newgame_rect.width/2,300)
    button_exit = pygame.image.load("assets/button_exit.bmp")
    button_exit_rect = button_exit.get_rect()
    button_exit_rect = button_exit_rect.move(SIZE[0] / 2 - button_exit_rect.width / 2, 400)


    # Initialise sprites
    pawnsprite = pygame.sprite.RenderPlain(pionek)
    backgroundsprite = pygame.sprite.RenderPlain(plansza)


    while 1:
        clock.tick(60)

        if mode == MENU:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if button_newgame_rect.collidepoint(position):
                        mode = GAMEPLAY_INITIALIZE
                    elif button_exit_rect.collidepoint(position):
                        sys.exit()

            screen.fill(BLACK)
            screen.blit(button_newgame, button_newgame_rect)
            screen.blit(button_exit, button_exit_rect)
            screen.blit(naglowek, naglowek_rect)
            pygame.display.flip()

        # GAMEPLAY mode _________________________________________________________________________________________________________________
        elif mode == GAMEPLAY:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    field = plansza.findSuitableField(position)
                    if field is not None:
                        pionek.posadzWPolu(field)
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        mode = MENU

            screen.fill(BLACK)
            screen.blit(background, (0, 0))
            screen.blit(background, plansza.rect, plansza.rect)
            screen.blit(background, pionek.rect, pionek.rect)
            backgroundsprite.draw(screen)
            pawnsprite.draw(screen)
            pygame.display.flip()

        elif mode == GAMEPLAY_INITIALIZE:

            mode = GAMEPLAY

        else:
            print "Zla wartosc mode"
            sys.exit(2)



if __name__ == '__main__': main()