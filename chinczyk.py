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
except ImportError as err:
    print("couldn't load module. %s" % err)
    sys.exit(2)


def czyPoleZajete(pionki, field):
    for pawn in pionki:
        if pawn.status == Pionek.Pionek.NA_PLANSZY:
            if pawn.pozycja == field:
                return pawn
    return False


def main():
    #Define constants
    global MENU
    global MENU_NEWGAME
    global GAMEPLAY
    global GAMEPLAY_INITIALIZE
    MENU = 0
    MENU_NEWGAME = 1
    GAMEPLAY = 2
    GAMEPLAY_INITIALIZE = 3
    SIZE = width, height = 500, 500
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

    # gameplay flags & variables
    global pionek_wybrany
    global numer_gracza
    global nastepnygracz
    global gracz
    global pionek
    global graczy

    # Initialize assets
    global grupaPionkow
    global grupaGraczy
    global grupaButtonowLosujacych
    global plansza
    plansza = Plansza.Plansza()
    backgroundsprite = pygame.sprite.Group(plansza)


    # Initialize menu assets
    naglowek = pygame.image.load("assets/naglowek.bmp")
    naglowek_rect = naglowek.get_rect()
    naglowek_rect = naglowek_rect.move(SIZE[0] / 2 - naglowek_rect.width / 2, 0)
    button_2graczy = pygame.image.load("assets/button_2_graczy.bmp")
    button_2graczy_rect = button_2graczy.get_rect()
    button_2graczy_rect = button_2graczy_rect.move(SIZE[0] / 2 - button_2graczy_rect.width / 2, 155)
    button_3graczy = pygame.image.load("assets/button_3_graczy.bmp")
    button_3graczy_rect = button_3graczy.get_rect()
    button_3graczy_rect = button_3graczy_rect.move(SIZE[0] / 2 - button_3graczy_rect.width / 2, 240)
    button_4graczy = pygame.image.load("assets/button_4_graczy.bmp")
    button_4graczy_rect = button_4graczy.get_rect()
    button_4graczy_rect = button_4graczy_rect.move(SIZE[0]/2-button_4graczy_rect.width/2,325)
    button_exit = pygame.image.load("assets/button_wyjscie.bmp")
    button_exit_rect = button_exit.get_rect()
    button_exit_rect = button_exit_rect.move(SIZE[0] / 2 - button_exit_rect.width / 2, 410)



    while 1:
        clock.tick(60)

        if mode == MENU:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if button_2graczy_rect.collidepoint(position):
                        graczy = 2
                        mode = GAMEPLAY_INITIALIZE
                    elif button_3graczy_rect.collidepoint(position):
                        graczy = 3
                        mode = GAMEPLAY_INITIALIZE
                    elif button_4graczy_rect.collidepoint(position):
                        graczy = 4
                        mode = GAMEPLAY_INITIALIZE
                    elif button_exit_rect.collidepoint(position):
                        sys.exit()

            screen.fill(BLACK)
            screen.blit(button_4graczy, button_4graczy_rect)
            screen.blit(button_3graczy, button_3graczy_rect)
            screen.blit(button_2graczy, button_2graczy_rect)
            screen.blit(button_exit, button_exit_rect)
            screen.blit(naglowek, naglowek_rect)
            pygame.display.flip()

        # NEW GAME initialization
        elif mode == GAMEPLAY_INITIALIZE:
            grupaPionkow = pygame.sprite.Group()
            grupaGraczy = pygame.sprite.Group()
            grupaButtonowLosujacych = pygame.sprite.Group()
            Gracz.Gracz(grupaPionkow, plansza, grupaGraczy, grupaButtonowLosujacych, Pionek.Pionek.ZOLTY)
            if graczy > 2:
                Gracz.Gracz(grupaPionkow, plansza, grupaGraczy, grupaButtonowLosujacych, Pionek.Pionek.CZERWONY)
            Gracz.Gracz(grupaPionkow, plansza, grupaGraczy, grupaButtonowLosujacych, Pionek.Pionek.NIEBIESKI)
            if graczy > 3:
                Gracz.Gracz(grupaPionkow, plansza, grupaGraczy, grupaButtonowLosujacych, Pionek.Pionek.ZIELONY)

            numer_gracza = 0
            gracz = grupaGraczy.sprites()[numer_gracza]
            pionek_wybrany = False
            nastepnygracz = False
            gracz.zaznacz()

            mode = GAMEPLAY

        # GAMEPLAY mode _________________________________________________________________________________________________________________
        elif mode == GAMEPLAY:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    field = plansza.findSuitableBoardField(position)
                    zawartosc = czyPoleZajete(grupaPionkow, field)

                    if plansza.hasPlayerClickedHisHome(gracz.kolor, position):
                        if gracz.wyjmijPionekZDomu():
                            if pionek_wybrany:
                                pionek.odznacz()
                                pionek = None
                                pionek_wybrany = False
                            nastepnygracz = True
                    elif gracz.kosc.rect.collidepoint(position):
                        print(gracz.kosc.losuj())
                    elif pionek_wybrany:
                        if plansza.hasPlayerClickedHisBase(gracz.kolor, position):
                            if pionek.posadzWBazie():
                                pionek_wybrany = False
                                nastepnygracz = True
                        elif field is not None:
                            if not zawartosc:
                                if pionek.posadzWPoluPlanszy(field):
                                    pionek_wybrany = False
                                    nastepnygracz = True
                            elif pionek == zawartosc:
                                pionek.odznacz()
                                pionek_wybrany = False
                    elif zawartosc is not False:
                        if zawartosc.gracz == gracz:
                            pionek = zawartosc
                            pionek.zaznacz()
                            pionek_wybrany = True

                    if nastepnygracz:
                        numer_gracza += 1
                        if numer_gracza == graczy:
                            numer_gracza = 0
                        gracz.odznacz()
                        gracz = grupaGraczy.sprites()[numer_gracza]
                        gracz.zaznacz()
                        nastepnygracz = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        mode = MENU

            screen.fill(BLACK)
            backgroundsprite.draw(screen)
            grupaPionkow.draw(screen)
            grupaGraczy.draw(screen)
            grupaButtonowLosujacych.draw(screen)
            pygame.display.flip()

        else:
            print("Zla wartosc mode")
            sys.exit(2)

if __name__ == '__main__': main()