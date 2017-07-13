import load
import pygame
import math
import Pionek


class Plansza(pygame.sprite.Sprite):

    # Defining constants
    FIELD_COORDS = [[405, 928], [405, 844], [405, 756], [405, 669], [405, 585], [302, 580], [220, 580], [138, 580], [62, 580], [62, 500],
                   [62, 410], [137, 410], [219, 410], [302, 410], [405, 405], [405, 316], [405, 228], [405, 140], [405, 60], [496, 60],
                   [583, 59], [583, 139], [583, 222], [583, 305], [583, 404], [662, 404], [750, 404], [838, 404], [920, 404], [920, 496],
                   [920, 583], [838, 583], [750, 583], [662, 583], [583, 585], [583, 669], [583, 754], [583, 838], [583, 930], [497, 928]]

    YELLOW_HOME = [[144, 936], [59, 936], [59, 840], [144, 840]]
    YELLOW_START = 0
    YELLOW_FINISH = 39
    YELLOW_BASE = [[494, 849], [494, 761], [494, 672], [494, 589]]

    RED_HOME = [[57, 146], [57, 62], [148, 62], [148, 146]]
    RED_START = 10
    RED_FINISH = 9
    RED_BASE = [[144, 498], [232, 498], [320, 498], [403, 498]]

    BLUE_HOME = [[830, 56], [924, 56], [924, 142], [830, 142]]
    BLUE_START = 20
    BLUE_FINISH = 19
    BLUE_BASE = [[493, 145], [493, 234], [493, 322], [493, 404]]

    GREEN_HOME = [[923, 844], [923, 935], [835, 935], [835, 844]]
    GREEN_START = 30
    GREEN_FINISH = 29
    GREEN_BASE = [[842, 496], [759, 496], [671, 496], [582, 496]]

    FIELD_RADIUS = 34

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load.load_png('assets/plansza_mala.bmp')
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        skala = 2
        self.FIELD_RADIUS /= skala

        for a in self.FIELD_COORDS:
            a[0] /= skala
            a[1] /= skala
        for a in self.YELLOW_HOME:
            a[0] /= skala
            a[1] /= skala
        for a in self.YELLOW_BASE:
            a[0] /= skala
            a[1] /= skala
        for a in self.RED_BASE:
            a[0] /= skala
            a[1] /= skala
        for a in self.RED_HOME:
            a[0] /= skala
            a[1] /= skala
        for a in self.BLUE_BASE:
            a[0] /= skala
            a[1] /= skala
        for a in self.BLUE_HOME:
            a[0] /= skala
            a[1] /= skala
        for a in self.GREEN_HOME:
            a[0] /= skala
            a[1] /= skala
        for a in self.GREEN_BASE:
            a[0] /= skala
            a[1] /= skala

    def findSuitableBoardField(self, point):
        # return field that the player meant when he clicked
        for i in range(0, len(Plansza.FIELD_COORDS)):
            if self.isClickpointNearby(Plansza.FIELD_COORDS[i], point):
                return i
        return None

    def hasPlayerClickedHisHome(self, color, point):
        if color == Pionek.Pionek.ZOLTY:
            for pole in self.YELLOW_HOME:
                if self.isClickpointNearby(pole, point):
                    return True
            return False
        elif color == Pionek.Pionek.CZERWONY:
            for pole in self.RED_HOME:
                if self.isClickpointNearby(pole, point):
                    return True
            return False
        elif color == Pionek.Pionek.NIEBIESKI:
            for pole in self.BLUE_HOME:
                if self.isClickpointNearby(pole, point):
                    return True
            return False
        elif color == Pionek.Pionek.ZIELONY:
            for pole in self.GREEN_HOME:
                if self.isClickpointNearby(pole, point):
                    return True
            return False
        else:
            raise AttributeError

    def findSuitableField(self, point):
        # return field that the player meant when he clicked
        for i in range(0,len(Plansza.FIELD_COORDS)):
            if self.isClickpointNearby(Plansza.FIELD_COORDS[i], point):
                return Plansza.FIELD_COORDS[i]

        for i in range(0,len(Plansza.YELLOW_HOME)):
            if self.isClickpointNearby(Plansza.YELLOW_HOME[i], point):
                return Plansza.YELLOW_HOME[i]

        for i in range(0,len(Plansza.YELLOW_BASE)):
            if self.isClickpointNearby(Plansza.YELLOW_BASE[i], point):
                return Plansza.YELLOW_BASE[i]

        for i in range(0,len(Plansza.RED_HOME)):
            if self.isClickpointNearby(Plansza.RED_HOME[i], point):
                return Plansza.RED_HOME[i]

        for i in range(0,len(Plansza.RED_BASE)):
            if self.isClickpointNearby(Plansza.RED_BASE[i], point):
                return Plansza.RED_BASE[i]

        for i in range(0,len(Plansza.BLUE_HOME)):
            if self.isClickpointNearby(Plansza.BLUE_HOME[i], point):
                return Plansza.BLUE_HOME[i]

        for i in range(0,len(Plansza.BLUE_BASE)):
            if self.isClickpointNearby(Plansza.BLUE_BASE[i], point):
                return Plansza.BLUE_BASE[i]

        for i in range(0,len(Plansza.GREEN_HOME)):
            if self.isClickpointNearby(Plansza.GREEN_HOME[i], point):
                return Plansza.GREEN_HOME[i]

        for i in range(0,len(Plansza.GREEN_BASE)):
            if self.isClickpointNearby(Plansza.GREEN_BASE[i], point):
                return Plansza.GREEN_BASE[i]

        return None

    def isClickpointNearby(self, field, point):
        return Plansza.FIELD_RADIUS > math.sqrt(math.pow(field[0]-point[0],2)+math.pow(field[1]-point[1],2))

