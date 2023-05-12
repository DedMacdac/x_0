play_field = [[" ", "1", "2", "3"],
              ["1", "-", "-", "-"],
              ["2", "-", "-", "-"],
              ["3", "-", "-", "-"]
              ]
condition = []


def x_0_info():
    for i in range(4):
        for j in range(4):
            print(play_field[i][j], end=" ")
        print()


def x_0_player1(x, y):
    global play_field
    play_field[x][y] = 'x'
    x_0_info()


def x_0_player2(x, y):
    global play_field
    play_field[x][y] = '0'
    x_0_info()


def player_1_turn():
    global condition
    p_1_x = int(input("\nPlayer1 enter the y coordinate "))
    p_1_y = int(input("\nPlayer1 enter the x coordinate "))
    x_0_player1(p_1_x, p_1_y)
    condition = [[play_field[1][1], play_field[2][2], play_field[3][3]],
                 [play_field[3][1], play_field[2][2], play_field[1][3]],
                 [play_field[1][1], play_field[2][1], play_field[3][1]],
                 [play_field[1][2], play_field[2][2], play_field[3][2]],
                 [play_field[1][3], play_field[2][3], play_field[3][3]],
                 [play_field[1][1], play_field[1][2], play_field[1][3]],
                 [play_field[2][1], play_field[2][2], play_field[2][3]],
                 [play_field[3][1], play_field[3][2], play_field[3][3]]]


def player_2_turn():
    global condition
    p_2_x = int(input("\nPlayer2 enter the y coordinate "))
    p_2_y = int(input("\nPlayer2 enter the x coordinate "))
    x_0_player2(p_2_x, p_2_y)
    condition = [[play_field[1][1], play_field[2][2], play_field[3][3]],
                 [play_field[3][1], play_field[2][2], play_field[1][3]],
                 [play_field[1][1], play_field[2][1], play_field[3][1]],
                 [play_field[1][2], play_field[2][2], play_field[3][2]],
                 [play_field[1][3], play_field[2][3], play_field[3][3]],
                 [play_field[1][1], play_field[1][2], play_field[1][3]],
                 [play_field[2][1], play_field[2][2], play_field[2][3]],
                 [play_field[3][1], play_field[3][2], play_field[3][3]]]


def check_vic():
    for n in condition:
        if n[2] == "x" and n[1] == "x" and n[0] == "x":
            print("\nCongratulations Player1 you're win!")
            return False
        elif n[0] == "0" and n[1] == "0" and n[2] == "0":
            print("\nCongratulations Player2 you're win!")
            return False
    return True


def check_tie():
    if "-" in play_field[0] or "-" in play_field[1] or "-" in play_field[2] or "-" in play_field[3]:
        return True
    else:
        print("\nits a tie, lucky next time")
        return False


def start_game():
    while check_tie() and check_vic():
        player_1_turn()
        check_vic()
        check_tie()
        if check_vic() and check_tie():
            player_2_turn()
            check_vic()
            check_tie()


start_game()
