import pygame
from blackJack.Button import Button
from blackJack.Game import Game
from blackJack.Player import Player
from blackJack.constants import BLACK, WHITE, GREEN, WIN, FPS, x_pos, button_y, space_x, PLAYER_NAME, DEALER_NAME, \
    DEALER_CONST


def button_array(text_list, x, y, space):
    button_list = []
    for text in text_list:
        button = Button(text, x, y, BLACK, WHITE)
        button_list.append(button)
        button.position()
        x += button.size[0] + space
    return button_list


def draw_window(player, button_list, game, dealer):
    WIN.fill(GREEN)
    if game.turn != DEALER_NAME:
        for button in button_list:
            button.draw(WIN)
    game.draw()
    player.draw()
    dealer.draw()

    pygame.display.update()


def event_check(buttons=None, game=None, player=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                button.click(game, player)
            game.check_win()
            return True
    return True


def pause(clock, player, game, dealer):
    while game.hold:
        print('pause')
        clock.tick(FPS)
        button_text = ["PLAY"]
        buttons = button_array(button_text, x_pos, button_y, space_x)
        event_check(buttons, game, player)
        draw_window(player, buttons, game, dealer)
        run = event_check(buttons, game, player)


def main():
    clock = pygame.time.Clock()
    run = True
    button_text = ["HIT", "STAND", "SPLIT", "SURRENDER", "BET"]
    buttons = button_array(button_text, x_pos, button_y, space_x)
    player = Player(PLAYER_NAME)
    dealer = Player(DEALER_NAME)
    game = Game(player, dealer)
    while run:

        clock.tick(FPS)

        if game.bet == 0:
            button_text = ["BET"]
            buttons = button_array(button_text, x_pos, button_y, space_x)
        if game.bet > 0 and game.turn == PLAYER_NAME:
            button_text = ['BET', "HIT", "STAND", "SPLIT", "SURRENDER"]
            buttons = button_array(button_text, x_pos, button_y, space_x)
        if game.bet > 0 and game.turn == PLAYER_NAME and len(player.cards) > 2:
            button_text = ["HIT", "STAND", "DOUBLE", "SPLIT", "SURRENDER"]
            buttons = button_array(button_text, x_pos, button_y, space_x)

        if player.bust:
            game.turn = DEALER_NAME

        while game.turn == DEALER_NAME:
            dealer.cards[0].flip = False
            draw_window(player, buttons, game, dealer)
            dealer.play(game)
            if dealer.score >= DEALER_CONST:
                game.turn = None
            pygame.time.delay(1000)
        player.calc_score()

        run = event_check(buttons, game, player)

        if not game.turn:
            print('check')
            game.check_win()
        draw_window(player, buttons, game, dealer)
        if game.winner or game.push:
            print('pay')
            pause(clock, player, game, dealer)
            player, dealer, game = game.pay()

    pygame.quit()


if __name__ == '__main__':
    main()
