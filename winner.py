def check_row(matrix):
    for row in matrix:
        if row[0] == row[1] and row[1] == row[2]:
            return row[0]
        else:
            continue


def check_column(matrix):
    row_one = matrix[0]
    row_two = matrix[1]
    row_three = matrix[2]

    i = 0
    for i in range(3):
        if row_one[i] == row_two[i] and row_two[i] == row_three[i]:
            return row_one[i]
        else:
            continue
        i += 1


def check_diagonal(matrix):
    row_one = matrix[0]
    row_two = matrix[1]
    row_three = matrix[2]

    if row_one[0] == row_two[1] and row_two[1] == row_three[2]:
        return row_one[0]
    elif row_one[2] == row_two[1] and row_two[1] == row_three[0]:
        return row_one[2]


def who_wins(matrix):
    winner = check_row(matrix)
    if not winner:
        winner = check_column(matrix)
    if not winner:
        winner = check_diagonal(matrix)
    if not winner:
        print("It's a draw!")
    else:
        print("The winner is player {}!".format(winner))


who_wins([[2, 0, 1],
          [0, 0, 0],
          [1, 0, 1]])
