from os import system, name


# Clear the screen


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def draw_board(game):
    roof = (" " + "-"*3)*3
    for row in game:
        print(roof)

        print("| " + str(row[0]) + " | " +
              str(row[1]) + " | " + str(row[2]) + " |")
    print(roof)


def take_input_from_player(player, game):
    try:
        player_input = input(
            "Player {} : where do you want to move [row,column]? ".format(player))
        draw = player_input.split(",")
        row, col = draw
        row = int(row) - 1
        col = int(col) - 1

        if game[row][col] == " ":
            game[row][col] = player

        else:
            print("Taken alredy, choose again.")
            take_input_from_player(player, game)

        clear()
        draw_board(game)

    except ValueError:
        print(
            "Invalid input (must be integer in [row, column] format). Try again.")
        take_input_from_player(player, game)


def check_if_finished(board):
    for sublist in board:
        if " " in sublist:
            return True
