import pygame
import load
import Pionek
import Plansza


class Gracz(pygame.sprite.Sprite):
    def __init__(self, pawnsGroup, plansza, grupaGraczy, kolor):
        pygame.sprite.Sprite.__init__(self)
        self.plansza = plansza
        self.pionki = pawnsGroup
        self.kolor = kolor
        self.moje_pionki = pygame.sprite.Group()
        self.dom = [0, 0, 0, 0]
        self.grupaGraczy = grupaGraczy

        if self.kolor == Pionek.Pionek.ZOLTY:
            self.start = self.plansza.YELLOW_START
            self.wspDomu = self.plansza.YELLOW_HOME
            self.imagestandard, self.imagestandardrect = load.load_png('assets/gracz_zolty.png')
            self.imageexcited, self.imageexcitedrect = load.load_png('assets/gracz_zolty_wzbudzony.png')
            self.imagestandardrect = self.imagestandardrect.move(10, 375 - self.imagestandardrect.height/2)
            self.imageexcitedrect = self.imageexcitedrect.move(10, 375 - self.imagestandardrect.height/2)
        elif self.kolor == Pionek.Pionek.NIEBIESKI:
            self.start = self.plansza.BLUE_START
            self.wspDomu = self.plansza.BLUE_HOME
            self.imagestandard, self.imagestandardrect = load.load_png('assets/gracz_niebieski.png')
            self.imageexcited, self.imageexcitedrect = load.load_png('assets/gracz_niebieski_wzbudzony.png')
            self.imagestandardrect = self.imagestandardrect.move(495 - self.imagestandardrect.width,
                                                                 120 - self.imagestandardrect.height / 2)
            self.imageexcitedrect = self.imageexcitedrect.move(495 - self.imagestandardrect.width,
                                                               120 - self.imagestandardrect.height / 2)
        elif self.kolor == Pionek.Pionek.CZERWONY:
            self.start = self.plansza.RED_START
            self.wspDomu = self.plansza.RED_HOME
            self.imagestandard, self.imagestandardrect = load.load_png('assets/gracz_czerwony.png')
            self.imageexcited, self.imageexcitedrect = load.load_png('assets/gracz_czerwony_wzbudzony.png')
            self.imagestandardrect = self.imagestandardrect.move(10,
                                                                 120 - self.imagestandardrect.height / 2)
            self.imageexcitedrect = self.imageexcitedrect.move(10,
                                                               120 - self.imagestandardrect.height / 2)
        elif self.kolor == Pionek.Pionek.ZIELONY:
            self.start = self.plansza.GREEN_START
            self.wspDomu = self.plansza.GREEN_HOME
            self.imagestandard, self.imagestandardrect = load.load_png('assets/gracz_zielony.png')
            self.imageexcited, self.imageexcitedrect = load.load_png('assets/gracz_zielony_wzbudzony.png')
            self.imagestandardrect = self.imagestandardrect.move(495 - self.imagestandardrect.width,
                                                                 375 - self.imagestandardrect.height / 2)
            self.imageexcitedrect = self.imageexcitedrect.move(495 - self.imagestandardrect.width,
                                                               375 - self.imagestandardrect.height / 2)

        for i in range(0, 4):
            self.moje_pionki.add(Pionek.Pionek(kolor, self, self.plansza))
            self.pionki.add(self.moje_pionki.sprites()[i])

        self.image = self.imagestandard
        self.rect = self.imagestandardrect
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()

        self.grupaGraczy.add(self)

    def wyjmijPionekZDomu(self):
        for pawn in self.moje_pionki:
            if pawn.status == Pionek.Pionek.W_DOMU:
                if pawn.wyjmijZDomu():
                    return pawn
        return False

    def zaznacz(self):
        self.image = self.imageexcited
        self.rect = self.imageexcitedrect

    def odznacz(self):
        self.image = self.imagestandard
        self.rect = self.imagestandardrect