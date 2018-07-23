from draw import clear, take_input_from_player, check_if_finished, draw_board
from winner import who_wins

# Set a while flag
playing = True

game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "], ]

player1 = "X"
player2 = "O"

clear()
draw_board(game)
while playing:

    winner = who_wins(game)
    if check_if_finished(game) and not winner:
        take_input_from_player(player1, game)

    winner = who_wins(game)
    if check_if_finished(game) and not winner:
        take_input_from_player(player2, game)

    if winner:
        playing = False

print("The winner is player {}!\n".format(winner))
