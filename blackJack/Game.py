import pygame

from blackJack.Player import Player
from blackJack.constants import BANK_FONT, WHITE, WIN, WIDTH, HEIGHT, PLAYER_NAME, DEALER_NAME, BLACKJACK_MULT, RED


class Game:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.hold = True
        self.push = None
        self.bet = 0
        self.turn = player.name
        self.winner = None

    def check_win(self):
        # for p in [self.player, self.dealer]:
        #     # if p.score == 21:
        #     #     p.blackjack = p.name
        #     # if p.score > 21:
        #     #     p.bust = p.name
        if self.dealer.bust and not self.player.bust:
            self.winner = self.player.name
            self.turn = None
        if self.player.bust and not self.dealer.bust:
            self.winner = self.dealer.name
            self.turn = None
        if self.player.bust and self.dealer.bust:
            self.push = True
            self.winner = None
            self.turn = None
        if self.player.blackjack and self.dealer.blackjack:
            self.push = True
            self.winner = None
        if self.push:
            print(f'push: {self.push}')
            self.winner = None

        if not self.turn and not self.player.bust and not self.dealer.bust and not self.winner and not self.push:
            if self.player.net_score > self.dealer.net_score:
                self.winner = self.dealer.name
            if self.dealer.net_score > self.player.net_score:
                self.winner = self.player.name
            if self.dealer == self.player:
                self.push = True
            if self.push:
                self.winner = 'PUSH'

    def draw(self):
        bank_text = BANK_FONT.render(
            "bet: $ " + str(self.bet), True, WHITE)
        text_width = bank_text.get_width()
        WIN.blit(bank_text, (WIDTH / 2 - text_width / 2, HEIGHT / 2))
        if self.hold:
            bank_text = BANK_FONT.render(
                "winner:" + str(self.winner), True, RED)
            text_width = bank_text.get_width()
            WIN.blit(bank_text, (WIDTH - text_width, HEIGHT / 10))

    def pay(self):
        print(f'{self.winner}: {self.player.bank}')
        if self.winner == self.player.name:
            self.player.bank += self.bet * 2
            self.bet = 0
        if self.player.blackjack and self.winner == self.player.name:
            self.player.bank += int(self.bet + self.bet * BLACKJACK_MULT)
            self.bet = 0

        if self.winner == self.dealer.name:
            self.bet = 0
        if self.push:
            self.player.bank += self.bet
            self.bet = 0
        chips = self.player.bank
        player = Player(PLAYER_NAME)
        player.bank = chips
        dealer = Player(DEALER_NAME)
        game = Game(player, dealer)

        return player, dealer, game
