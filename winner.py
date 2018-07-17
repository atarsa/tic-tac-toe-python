def check_row(matrix):
    for row in matrix:
        if row[0] == row[1] and row[1] == row[2]:
            winner = row[0]
            return winner
        else:
            continue


def check_column(matrix):
    row_one = matrix[0]
    row_two = matrix[1]
    row_three = matrix[2]

    i = 0
    for i in range(3):
        if row_one[i] == row_two[i] and row_two[i] == row_three[i]:
            winner = row_one[i]
            return winner
        else:
            continue
        i += 1


def check_diagonal(matrix):
    row_one = matrix[0]
    row_two = matrix[1]
    row_three = matrix[2]

    if row_one[0] == row_two[1] and row_two[1] == row_three[2]:
        winner = row_one[0]
        return winner
    elif row_one[2] == row_two[1] and row_two[1] == row_three[0]:
        winner = row_one[2]
        return winner


def who_wins(matrix):
    check_row(matrix)
    check_column(matrix)
    check_diagonal(matrix)

    if winner:
        print(winner)
    else:
        print("It's a draw!")


who_wins([[1, 1, 1],
          [2, 2, 0],
          [2, 1, 1]])
