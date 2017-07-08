import pygame
import load
import Pionek
import Plansza


class Gracz():
    def __init__(self, playersGroup, pawnsGroup, plansza, kolor):
        self.gracze = playersGroup
        self.plansza = plansza
        self.pionki = pawnsGroup
        self.kolor = kolor
        self.moje_pionki = pygame.sprite.Group()

        if self.kolor == Pionek.Pionek.ZOLTY:
            self.moje_pionki.add(Pionek.Pionek(Plansza.Plansza.YELLOW_HOME[0],kolor,self))
            self.pionki.add(self.moje_pionki[0])
            self.moje_pionki.add(Pionek.Pionek(Plansza.Plansza.YELLOW_HOME[1], kolor, self))
            self.pionki.add(self.moje_pionki[1])
            self.moje_pionki.add(Pionek.Pionek(Plansza.Plansza.YELLOW_HOME[2], kolor, self))
            self.pionki.add(self.moje_pionki[2])
            self.moje_pionki.add(Pionek.Pionek(Plansza.Plansza.YELLOW_HOME[3], kolor, self))
            self.pionki.add(self.moje_pionki[3])

