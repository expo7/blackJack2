import pygame
from blackJack.Button import Button
from blackJack.Game import Game
from blackJack.Player import Player
from blackJack.constants import BLACK, WHITE, GREEN, WIN, FPS, x_pos, button_y, space_x, PLAYER_NAME, DEALER_NAME


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
    player.draw()
    dealer.draw()
    game.draw()
    pygame.display.update()


def event_check(buttons=None, game=None, player=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                button.click(game, player)
            player.calc_score()
            game.check_win()
            return True
    return True


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

        if game.turn == DEALER_NAME:
            pygame.time.delay(1000)
            draw_window(player, buttons, game, dealer)
            button_text = ['play again!']
            buttons = button_array(button_text, x_pos, button_y, space_x)
            dealer.play(game)
            game.check_win()
            game.turn = None
        run = event_check(buttons, game, player)
        draw_window(player, buttons, game, dealer)
        if game.winner or game.push:
            player, dealer, game = game.pay()

    pygame.quit()


if __name__ == '__main__':
    main()
