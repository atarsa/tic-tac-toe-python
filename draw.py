game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0], ]

player1 = "X"
player2 = "O"


def take_input_from_player(player):
    player_input = input(
        "{} : where do you want to move [row,column]? ".format(player))
    draw = player_input.split(",")

    row, col = draw
    row = int(row) - 1
    col = int(col) - 1

    if game[row][col] == 0:
        game[row][col] = player
    else:
        print("Taken alredy, choose again.")
        take_input_from_player(player)
    print(game)


while True:

    take_input_from_player(player1)
    take_input_from_player(player2)
