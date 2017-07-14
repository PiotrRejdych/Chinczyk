import pygame
import load
import Pionek
import Plansza
import ButtonLosujacy


class Gracz(pygame.sprite.Sprite):
    def __init__(self, pawnsGroup, plansza, grupaGraczy, grupaButtonowLosujacych, kolor):
        pygame.sprite.Sprite.__init__(self)
        self.plansza = plansza
        self.pionki = pawnsGroup
        self.kolor = kolor
        self.moje_pionki = pygame.sprite.Group()
        self.dom = [0, 0, 0, 0]
        self.baza = [0, 0, 0, 0]
        self.grupaGraczy = grupaGraczy
        self.grupaButtonow = grupaButtonowLosujacych

        if self.kolor == Pionek.Pionek.ZOLTY:
            self.start = self.plansza.YELLOW_START
            self.wspDomu = self.plansza.YELLOW_HOME
            self.wspBazy = self.plansza.YELLOW_BASE
            self.finisz = self.plansza.YELLOW_FINISH
            self.imagestandard, self.imagestandardrect = load.load_png('assets/gracz_zolty.png')
            self.imageexcited, self.imageexcitedrect = load.load_png('assets/gracz_zolty_wzbudzony1.png')
            self.imagestandardrect = self.imagestandardrect.move(12, 375 - self.imagestandardrect.height/2)
            self.imageexcitedrect = self.imageexcitedrect.move(10, 375 - self.imageexcitedrect.height/2)
        elif self.kolor == Pionek.Pionek.NIEBIESKI:
            self.start = self.plansza.BLUE_START
            self.wspDomu = self.plansza.BLUE_HOME
            self.wspBazy = self.plansza.BLUE_BASE
            self.finisz = self.plansza.BLUE_FINISH
            self.imagestandard, self.imagestandardrect = load.load_png('assets/gracz_niebieski.png')
            self.imageexcited, self.imageexcitedrect = load.load_png('assets/gracz_niebieski_wzbudzony1.png')
            self.imagestandardrect = self.imagestandardrect.move(493 - self.imagestandardrect.width,
                                                                 120 - self.imagestandardrect.height / 2)
            self.imageexcitedrect = self.imageexcitedrect.move(495 - self.imageexcitedrect.width,
                                                               120 - self.imageexcitedrect.height / 2)
        elif self.kolor == Pionek.Pionek.CZERWONY:
            self.start = self.plansza.RED_START
            self.wspDomu = self.plansza.RED_HOME
            self.wspBazy = self.plansza.RED_BASE
            self.finisz = self.plansza.RED_FINISH
            self.imagestandard, self.imagestandardrect = load.load_png('assets/gracz_czerwony.png')
            self.imageexcited, self.imageexcitedrect = load.load_png('assets/gracz_czerwony_wzbudzony1.png')
            self.imagestandardrect = self.imagestandardrect.move(12,
                                                                 120 - self.imagestandardrect.height / 2)
            self.imageexcitedrect = self.imageexcitedrect.move(10,
                                                               120 - self.imageexcitedrect.height / 2)
        elif self.kolor == Pionek.Pionek.ZIELONY:
            self.start = self.plansza.GREEN_START
            self.wspDomu = self.plansza.GREEN_HOME
            self.wspBazy = self.plansza.GREEN_BASE
            self.finisz = self.plansza.GREEN_FINISH
            self.imagestandard, self.imagestandardrect = load.load_png('assets/gracz_zielony.png')
            self.imageexcited, self.imageexcitedrect = load.load_png('assets/gracz_zielony_wzbudzony1.png')
            self.imagestandardrect = self.imagestandardrect.move(493 - self.imagestandardrect.width,
                                                                 375 - self.imagestandardrect.height / 2)
            self.imageexcitedrect = self.imageexcitedrect.move(495 - self.imageexcitedrect.width,
                                                               375 - self.imageexcitedrect.height / 2)

        for i in range(0, 4):
            self.moje_pionki.add(Pionek.Pionek(kolor, self, self.plansza))
            self.pionki.add(self.moje_pionki.sprites()[i])

        self.kosc = ButtonLosujacy.ButtonLosujacy(kolor, self.grupaButtonow)

        self.image = self.imagestandard
        self.rect = self.imagestandardrect
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()

        self.grupaGraczy.add(self)

    def wyjmijPionekZDomu(self):
        if self.plansza.czyPoleZajete(self.pionki, self.start) is False:
            for pawn in self.moje_pionki:
                if pawn.status == Pionek.Pionek.W_DOMU:
                    if pawn.wyjmijZDomu():
                        return pawn
            return False
        return False

    def zaznacz(self):
        self.image = self.imageexcited
        self.rect = self.imageexcitedrect
        self.kosc.zaznacz()

    def odznacz(self):
        self.image = self.imagestandard
        self.rect = self.imagestandardrect
        self.kosc.odznacz()