import os
import pygame

PLAYER_NAME = 'Brendan'
DEALER_NAME = 'dealer'
BLACKJACK_MULT = 3 / 2
CARD_SHIFT = 20
CHIP = 20
BANK = 1000
DEALER_CONST = 17

pygame.font.init()
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BANK_FONT = pygame.font.SysFont('Arial', 20)
BUTTON_FONT = pygame.font.SysFont('Arial', 20)
pygame.init()

pygame.display.set_caption('Blackjack')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (100, 100, 100)
GREEN = (0, 100, 0)
BLUE = (0, 0, 255)
RED=(255,0,0)
FPS = 40
values = list(range(2, 11))
BACK_IMG = pygame.image.load(os.path.join('cards', 'back.png'))
CARD_WIDTH = BACK_IMG.get_width() + 10
scores = []
symbols = ['c', 'd', 'h', 's']
faces = ['j', 'q', 'k', 'a']
aces = ['ca', 'da', 'ha', 'sa']
deck = []

for s in symbols:
    for val in values:
        deck.append(s + str(val))
        scores.append(val)

    for face in faces:
        if face == 'a':
            deck.append(s + str(face))
            scores.append(11)
        else:
            deck.append(s + str(face))
            scores.append(10)

deck_dict = dict(zip(deck, scores))
x_pos = 120
space_x = 20
button_y = 5
