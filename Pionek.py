import load
import pygame
import sys


class Pionek(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    # Defining constants
    ZOLTY = 0
    CZERWONY = 1
    NIEBIESKI = 2
    ZIELONY = 3

    def __init__(self, vector, color, gracz):
        pygame.sprite.Sprite.__init__(self)
        self.moj_kolor = color
        self.gracz = gracz
        if self.moj_kolor == Pionek.ZOLTY:
            self.image, self.rect = load.load_png('assets/pionek_zolty.png')
        elif self.moj_kolor == Pionek.CZERWONY:
            self.image, self.rect = load.load_png('assets/pionek_czerwony.png')
        elif self.moj_kolor == Pionek.NIEBIESKI:
            self.image, self.rect = load.load_png('assets/pionek_niebieski.png')
        elif self.moj_kolor == Pionek.ZIELONY:
            self.image, self.rect = load.load_png('assets/pionek_zielony.png')
        else:
            print "Zly numer koloru pionka"
            raise AttributeError
            sys.exit(2)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0

    def posadzWPolu(self, point):
        self.rect = self.rect.move(point[0]-self.rect.left-self.rect.width/2, point[1]-self.rect.top-self.rect.height/2)