import pygame
import load
import Pionek
import random


class ButtonLosujacy(pygame.sprite.Sprite):
    def __init__(self, kolor, grupaButtonowLosujacych):
        pygame.sprite.Sprite.__init__(self)
        self.kolor = kolor
        self.grupa = grupaButtonowLosujacych

        self.images = [load.load_png('assets/Dice_x.png'), load.load_png('assets/Dice_1.png'),
                       load.load_png('assets/Dice_2.png'), load.load_png('assets/Dice_3.png'),
                       load.load_png('assets/Dice_4.png'), load.load_png('assets/Dice_5.png'),
                       load.load_png('assets/Dice_6.png')]
        self.imageinactive = load.load_png('assets/Dice_0.png')

        self.image, self.rect = self.imageinactive
        self.zaznaczony = False

        if self.kolor == Pionek.Pionek.ZOLTY:
            self.rect = self.rect.move(143 - self.rect.width/2, 354 - self.rect.height/2)
        elif self.kolor == Pionek.Pionek.NIEBIESKI:
            self.rect = self.rect.move(346 - self.rect.width/2, 148 - self.rect.height/2)
        elif self.kolor == Pionek.Pionek.CZERWONY:
            self.rect = self.rect.move(140 - self.rect.width/2, 47 - self.rect.height/2)
        elif self.kolor == Pionek.Pionek.ZIELONY:
            self.rect = self.rect.move(353 - self.rect.width/2, 451 - self.rect.height/2)

        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()

        self.grupa.add(self)

        random.seed()

    def zaznacz(self):
        self.zaznaczony = True
        self.image = self.images[0][0]

    def odznacz(self):
        self.zaznaczony = False
        self.image = self.imageinactive[0]

    def losuj(self):
        wynik = random.randint(1,6)
        self.image = self.images[wynik][0]
        return wynik