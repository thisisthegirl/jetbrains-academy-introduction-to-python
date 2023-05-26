matrix = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def table():
    print("---------")
    print("| " + matrix[0][0] + " " + matrix[0][1] + " " + matrix[0][2] + " |")
    print("| " + matrix[1][0] + " " + matrix[1][1] + " " + matrix[1][2] + " |")
    print("| " + matrix[2][0] + " " + matrix[2][1] + " " + matrix[2][2] + " |")
    print("---------")


counter = 1


def round_one():
    move = str(input())

    coordinates = move.split(" ")

    try:
        global counter
        a = int(coordinates[0]) - 1
        b = int(coordinates[1]) - 1
        if matrix[a][b] != "_":
            print("This cell is occupied! Choose another one!")
            round_one()
        else:
            if counter % 2 == 1:
                matrix[a][b] = "X"
                counter += 1
            elif counter % 2 == 0:
                matrix[a][b] = "O"
                counter += 1
    except ValueError:
        print("You should enter numbers!")
        round_one()
    except IndexError:
        print("Coordinates should be from 1 to 3!")
        round_one()


while True:
    table()

    if counter > 9:
        print("Draw")
        break

    round_one()

    list_symbols = [symbol for row in matrix for symbol in row]
    count_x = list_symbols.count("X")
    count_o = list_symbols.count("O")

    if abs(count_x - count_o) not in (-1, 0, 1):
        print("Impossible")
        break

    winning_patterns = [
        list_symbols[0:3], list_symbols[3:6], list_symbols[6:9],
        list_symbols[0::3], list_symbols[1::3], list_symbols[2::3],
        list_symbols[0::4], list_symbols[2:8:2]
    ]

    if any(pattern == ["X", "X", "X"] for pattern in winning_patterns):
        if any(pattern == ["O", "O", "O"] for pattern in winning_patterns):
            print("Impossible")
            break
        table()
        print("X wins")
        break

    if any(pattern == ["O", "O", "O"] for pattern in winning_patterns):
        table()
        print("O wins")
        break
