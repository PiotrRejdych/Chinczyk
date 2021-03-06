import load
import pygame
import sys


class Pionek(pygame.sprite.Sprite):
    # Defining constants
    ZOLTY = 0
    CZERWONY = 1
    NIEBIESKI = 2
    ZIELONY = 3

    W_DOMU = 0
    NA_PLANSZY = 1
    W_BAZIE = 2

    def __init__(self, color, gracz, plansza):
        pygame.sprite.Sprite.__init__(self)
        self.kolor = color
        self.gracz = gracz
        self.plansza = plansza
        if self.kolor == Pionek.ZOLTY:
            self.imagestandard, self.rectstandard = load.load_png('assets/pionek_zolty_maly.png')
            self.imageexcited, self.rectexcited = load.load_png('assets/pionek_zolty_maly_podekscytowany.png')
            self.image = self.imagestandard
            self.rect = self.rectstandard
        elif self.kolor == Pionek.CZERWONY:
            self.imagestandard, self.rectstandard = load.load_png('assets/pionek_czerwony_maly.png')
            self.imageexcited, self.rectexcited = load.load_png('assets/pionek_czerwony_maly_podekscytowany.png')
            self.image = self.imagestandard
            self.rect = self.rectstandard
        elif self.kolor == Pionek.NIEBIESKI:
            self.imagestandard, self.rectstandard = load.load_png('assets/pionek_niebieski_maly.png')
            self.imageexcited, self.rectexcited = load.load_png('assets/pionek_niebieski_maly_podekscytowany.png')
            self.image = self.imagestandard
            self.rect = self.rectstandard
        elif self.kolor == Pionek.ZIELONY:
            self.imagestandard, self.rectstandard = load.load_png('assets/pionek_zielony_maly.png')
            self.imageexcited, self.rectexcited = load.load_png('assets/pionek_zielony_maly_podekscytowany.png')
            self.image = self.imagestandard
            self.rect = self.rectstandard
        else:
            print("Zly numer koloru pionka")
            raise AttributeError
            sys.exit(2)
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.hit = 0
        self.status = None
        self.pozycja = None
        self.zaznaczony = False
        self.posadzWDomu()

    def posadzWPunkcie(self, point):
        self.rectstandard = self.rectstandard.move(point[0]-self.rectstandard.left-self.rectstandard.width/2, point[1]-self.rectstandard.top-self.rectstandard.height/2)
        self.rectexcited = self.rectexcited.move(point[0] - self.rectexcited.left - self.rectexcited.width / 2,
                                                     point[1] - self.rectexcited.top - self.rectexcited.height / 2)
        self.rect = self.rect.move(point[0] - self.rect.left - self.rect.width / 2,
                                   point[1] - self.rect.top - self.rect.height / 2)

    def posadzWPoluPlanszy(self, field):
        if self.status == Pionek.NA_PLANSZY:
            self.posadzWPunkcie(self.plansza.FIELD_COORDS[field])
            self.pozycja = field
            self.odznacz()
            return True
        return False
        #self.rect = self.rect.move(self.plansza.FIELD_COORDS[field][0]-self.rect.left-self.rect.width/2, self.plansza.FIELD_COORDS[field][1]-self.rect.top-self.rect.height/2)

    def wyznaczCel(self, fieldcount):
        if self.status == self.NA_PLANSZY:
            if self.pozycja + fieldcount >= 40:
                if self.gracz.finisz == 39:
                    return 40
                else:
                    return self.pozycja + fieldcount - 40
            else:
                if self.pozycja > self.gracz.finisz:
                    return self.pozycja + fieldcount
                elif self.pozycja + fieldcount > self.gracz.finisz:
                    return 40 # 40 oznacza wejście do bazy
                else:
                    return self.pozycja + fieldcount
        else:
            raise AttributeError

    def narysujDrogeA(self, fieldcount, ekran):
        self.narysujDroge(self.wyznaczCel(fieldcount), ekran)

    def narysujDroge(self, field, ekran):
        if self.status == self.NA_PLANSZY:
            if field == 40: #wrzut do bazy
                punkty = [self.plansza.FIELD_COORDS[self.pozycja]]
                if self.pozycja > self.gracz.finisz:
                    for i in range(self.pozycja+1, len(self.plansza.FIELD_COORDS)):
                        punkty.append(self.plansza.FIELD_COORDS[i])
                    for i in range(0, self.gracz.finisz+1):
                        punkty.append(self.plansza.FIELD_COORDS[i])
                else:
                    for i in range(self.pozycja, self.gracz.finisz):
                        punkty.append(self.plansza.FIELD_COORDS[i+1])
                punkty.append(self.gracz.wspBazy[0])

                pygame.draw.lines(ekran, self.kolor, False, punkty, 3)
            elif 0 <= field < 40:
                punkty = [self.plansza.FIELD_COORDS[self.pozycja]]
                if self.pozycja > field:
                    for i in range(self.pozycja + 1, len(self.plansza.FIELD_COORDS)):
                        punkty.append(self.plansza.FIELD_COORDS[i])
                    for i in range(0, field + 1):
                        punkty.append(self.plansza.FIELD_COORDS[i])
                else:
                    for i in range(self.pozycja, field):
                        punkty.append(self.plansza.FIELD_COORDS[i + 1])

                pygame.draw.lines(ekran, self.kolor, False, punkty, 3)
            else:
                raise AttributeError
        else:
            raise AttributeError

    def zbity(self):
        if self.status == Pionek.NA_PLANSZY:
            self.posadzWDomu()
            return True
        return False

    def zaznacz(self):
        self.zaznaczony = True
        self.image = self.imageexcited
        self.rect = self.rectexcited

    def odznacz(self):
        self.zaznaczony = False
        self.image = self.imagestandard
        self.rect = self.rectstandard

    def posadzWDomu(self):
        for i in range(0, len(self.gracz.dom)):
            if self.gracz.dom[i] == 0:
                self.gracz.dom[i] = 1
                self.posadzWPunkcie(self.gracz.wspDomu[i])
                self.status = Pionek.W_DOMU
                self.pozycja = None
                return True
        return False

    def wyjmijZDomu(self):
        if self.status == Pionek.W_DOMU:
            for i in range(0, len(self.gracz.dom)):
                if self.gracz.dom[i] == 1:
                    self.gracz.dom[i] = 0
                    self.status = Pionek.NA_PLANSZY
                    self.posadzWPoluPlanszy(self.gracz.start)
                    return True
        return False

    def posadzWBazie(self):
        if self.status == Pionek.NA_PLANSZY:
            i = 4
            while i > 0:
                i -= 1
                if self.gracz.baza[i] == 0:
                    self.gracz.baza[i] = 1
                    self.status = Pionek.W_BAZIE
                    self.pozycja = None
                    self.odznacz()
                    self.posadzWPunkcie(self.gracz.wspBazy[i])
                    return True
            return False
        return False