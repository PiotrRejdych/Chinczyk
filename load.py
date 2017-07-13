import pygame


def load_png(name):
    """ Load image and return image object"""
    fullname = name
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise SystemExit
    return image, image.get_rect()


def load_bmp(name):
    """ Load image and return image object"""
    fullname = name
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise SystemExit
    return image, image.get_rect()