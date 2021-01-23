import random

import pygame

from blackJack.Card import Card
from blackJack.constants import WIDTH, WIN, BANK_FONT, WHITE, HEIGHT, deck, aces, CARD_WIDTH, BACK_IMG, CARD_SHIFT


class Player:
    def __init__(self, name):
        self.name = name
        self.make_bet = None
        self.blackjack = None
        self.bust = None
        self.bank = 1000
        self.cards = self.deal()
        self.score = self.calc_score()
        self.net_score = 21 - self.score

    def deal(self):
        # card1=Card()
        # card2=Card()

        card1 = Card(deck[random.randint(0, len(deck) - 1)])
        card2 = Card(deck[random.randint(0, len(deck) - 1)])
        if self.name == 'dealer':
            card1.flip = True
        return [card1, card2]

    def calc_score(self):
        self.score = 0
        for card in self.cards:
            if not card.flip:
                self.score += card.val
        for card in self.cards:
            if self.score > 21 and str(card) in aces:
                self.score -= 10
        return self.score

    def play(self, game):
        self.cards[0].flip = False
        self.calc_score()
        while self.score < 17:
            pygame.time.delay(1000)
            self.cards.append(Card(deck[random.randint(0, len(deck) - 1)]))
            self.calc_score()

        self.calc_score()
        while self.score < 17:
            pygame.time.delay(1000)
            self.cards.append(Card(deck[random.randint(0, len(deck) - 1)]))
            self.calc_score()
        self.net_score = 21 - self.score
        game.turn = None

    def draw(self):
        x = WIDTH / 2 - CARD_WIDTH - 100
        y = 100

        if self.name == 'dealer':
            score_text = BANK_FONT.render(
                "dealer score: " + str(self.score), True, WHITE)
            text_width = score_text.get_width()
            WIN.blit(score_text, (WIDTH / 4 - text_width / 2, 25))

            for card in self.cards:
                if not card.flip:
                    WIN.blit(card.img, (x, y))
                    x += CARD_SHIFT
                    y -= CARD_SHIFT
                else:
                    WIN.blit(BACK_IMG, (x, y))
                    x += CARD_SHIFT
                    y -= CARD_SHIFT

        else:
            bank_text = BANK_FONT.render(
                "chips: $ " + str(self.bank), True, WHITE)
            text_width = bank_text.get_width()
            WIN.blit(bank_text, (WIDTH / 2 - text_width / 2, HEIGHT - 100))
            score_text = BANK_FONT.render(
                "score: " + str(self.score), True, WHITE)
            text_width = score_text.get_width()
            WIN.blit(score_text, (WIDTH / 4 - text_width / 2, HEIGHT - 100))
            y = 350
            for card in self.cards:
                if not card.flip:
                    WIN.blit(card.img, (x, y))
                    x += CARD_SHIFT
                    y -= CARD_SHIFT
                else:
                    WIN.blit(BACK_IMG, (x, y))
                    x += CARD_SHIFT
                    y -= CARD_SHIFT
