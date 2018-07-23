def draw_roof(tiles):
    roof = " " + "-"*3
    print(roof*tiles)


def draw_wall(tiles):
    print("|   "*(tiles+1))


def draw_row(rows):
    for row in range(rows):
        draw_roof(rows)
        draw_wall(rows)
    draw_roof(rows)


# size = input("What size game board do you want to draw? ")
