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
    global wynik_na_kosci
    global drugi_rzut_po_6
    global drugi_rzut_po_6_wykorzystany
    global trzy_rzuty
    global wygral
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

    # initialize win screens
    win_screens = [load.load_png('assets/wygrana_zolty.png'), load.load_png('assets/wygrana_czerwony.png'), load.load_png('assets/wygrana_niebieski.png'), load.load_png('assets/wygrana_zielony.png') ]

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
            wynik_na_kosci = 0
            drugi_rzut_po_6 = False
            drugi_rzut_po_6_wykorzystany = False
            trzy_rzuty = 0
            wygral = None
            gracz.zaznacz()

            mode = GAMEPLAY

        # GAMEPLAY mode _________________________________________________________________________________________________________________
        elif mode == GAMEPLAY:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if wygral is not None:
                        mode = MENU
                    # obsluga trzech rzutow dla gracza ktory nie ma pionkow na planszy
                    elif wynik_na_kosci != 0 and wynik_na_kosci != 6 and not gracz.czyGraczMaPionkiNaPlanszy() and not drugi_rzut_po_6:
                        if trzy_rzuty == 2:
                            nastepnygracz = True
                        elif gracz.kosc.rect.collidepoint(position):
                            wynik_na_kosci = gracz.kosc.losuj()
                            trzy_rzuty += 1
                    # obsluga rzutu koscia, byc moze drugiego z kolei po wyrzuceniu 6
                    elif wynik_na_kosci == 0 and gracz.kosc.rect.collidepoint(position):
                        if drugi_rzut_po_6:
                            wynik_na_kosci = gracz.kosc.losuj()
                            drugi_rzut_po_6 = False
                            drugi_rzut_po_6_wykorzystany = True
                        else:
                            wynik_na_kosci = gracz.kosc.losuj()
                    # wyprowadzenie pionka z domu
                    elif wynik_na_kosci == 6 and plansza.hasPlayerClickedHisHome(gracz.kolor, position):
                        if gracz.wyjmijPionekZDomu():
                            if pionek_wybrany:
                                pionek.odznacz()
                                pionek = None
                                pionek_wybrany = False
                            nastepnygracz = True
                    elif wynik_na_kosci != 0:
                        # wprowadzenie pionka do bazy
                        if pionek_wybrany and plansza.hasPlayerClickedHisBase(gracz.kolor, position) and pionek.wyznaczCel(wynik_na_kosci) == 40:
                            if pionek.posadzWBazie():
                                pionek_wybrany = False
                                pionek.odznacz()
                                pionek = None
                                if gracz.czyGraczZapelnilBaze():
                                    wygral = gracz
                                else:
                                    nastepnygracz = True
                        else:
                        # inne poruszanie po planszy, zbijanie pionkow, zaznaczanie swoich pionkow
                            field = plansza.findSuitableBoardField(position)
                            if field is not None:
                                zawartosc = plansza.czyPoleZajete(grupaPionkow, field)
                                if zawartosc is not False:
                                    if pionek_wybrany:
                                        if pionek == zawartosc:
                                            pionek.odznacz()
                                            pionek_wybrany = False
                                            pionek = None
                                        elif pionek.gracz == zawartosc.gracz:
                                            pionek.odznacz()
                                            pionek = zawartosc
                                            pionek.zaznacz()
                                        elif pionek.wyznaczCel(wynik_na_kosci) == field:
                                            if zawartosc.zbity():
                                                if pionek.posadzWPoluPlanszy(field):
                                                    pionek.odznacz()
                                                    pionek_wybrany = False
                                                    pionek = None
                                                    nastepnygracz = True
                                    elif zawartosc.gracz == gracz:
                                        pionek = zawartosc
                                        pionek_wybrany = True
                                        pionek.zaznacz()
                                elif pionek_wybrany:
                                    if pionek.wyznaczCel(wynik_na_kosci) == field:
                                        if pionek.posadzWPoluPlanszy(field):
                                            pionek.odznacz()
                                            pionek_wybrany = False
                                            pionek = None
                                            nastepnygracz = True


                    if nastepnygracz:
                        if wynik_na_kosci == 6 and not drugi_rzut_po_6_wykorzystany and trzy_rzuty == 0:
                            drugi_rzut_po_6 = True
                            nastepnygracz = False
                            wynik_na_kosci = 0
                            gracz.kosc.ustawzero()
                        else:
                            drugi_rzut_po_6 = False
                            drugi_rzut_po_6_wykorzystany = False
                            wynik_na_kosci = 0
                            trzy_rzuty = 0
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
            if pionek_wybrany:
                pionek.narysujDrogeA(wynik_na_kosci, screen)
            if wygral is not None:
                screen.blit(win_screens[wygral.kolor][0], win_screens[wygral.kolor][1])
            pygame.display.flip()

        else:
            print("Zla wartosc mode")
            sys.exit(2)

if __name__ == '__main__': main()