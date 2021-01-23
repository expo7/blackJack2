import os

import pygame

from blackJack.constants import deck_dict, WIN


class Card:

    def __init__(self, name):
        self.name = name
        self.flip = False
        self.val = deck_dict[name]
        self.img = pygame.image.load(os.path.join('cards', name + '.png'))

    def draw(self):
        if not self.flip:
            WIN.blit(self.img, (100, 100))

    def __repr__(self):
        return str(self.name)