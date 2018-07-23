game = [[1, 2, 1],
        [1, 1, 1],
        [1, 1, 0], ]


def check(board):
    for sublist in board:

        if 0 in sublist:
            print("it's here")
        else:
            print("NOT THIS TIME :<")


check(game)
