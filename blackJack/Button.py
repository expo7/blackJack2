import random

import pygame

from blackJack.Card import Card
from blackJack.constants import deck, CHIP

pygame.font.init()
pygame.mixer.init()

# from .constants import deck

HEIGHT = 600
BUTTON_FONT = pygame.font.SysFont("Arial", 20)


class Button:
    def __init__(self, text, x, y, background_color, text_color):
        self.x = x
        self.y = y
        self.padding = 10
        self.background_color = background_color
        self.text_color = text_color
        self.text = text
        self.size = BUTTON_FONT.render(text, True, self.text_color).get_size()
        self.rect = pygame.Rect((self.x, self.y), self.size)

    def position(self):
        self.y = HEIGHT - self.size[1] - 15
        self.rect = pygame.Rect((self.x - self.padding, self.y - self.padding),
                                (self.size[0] + self.padding, self.size[1] + self.padding))

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.background_color, self.rect)
        text = BUTTON_FONT.render(self.text, True, self.text_color)
        WIN.blit(text, (self.x - self.padding / 2, self.y - self.padding / 2))

    def click(self, game, player):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            if self.text == "BET":
                if player.bank >= CHIP:
                    game.bet += CHIP
                    player.bank -= CHIP
            if self.text == "HIT":
                player.cards.append(Card(deck[random.randint(0, len(deck) - 1)]))

            if self.text == 'STAND':
                game.turn = 'dealer'
                player.net_score = 21 - player.score
            if self.text == 'PLAY':
                game.hold = False
            if self.text == 'DOUBLE':
                game.bet += game.bet
                player.bank -= game.bet
