print("This Is Tic Tac Toe")
print("Please Enter Which Position Number You Want To Play")

player_turn = 1

# 0 = continue, 1 = player 1 win, 2 = player 2 win, 3 = draw
game_status = 0

board = ["1", "2",  "3",  "4",  "5",  "6",  "7", "8",  "9"]

# board is printed in rows of 3
# each row has 3 elements
# print exactly what's in the list
def print_board():
    counter = 0
    for i in board:
        if counter < 3:
            print(board[0:3])
        elif counter < 6:
            print(board[3:6])
        elif counter < 9:
            print(board[6:9])
        counter += 3

def check_win():
    # these are all the possible conbinations that can win with
    win_cases = [
        # rows
        board[0:3], board[3:6], board[6:9],
        # 1st column
        [board[0], board[3], board[6]],
        # 2nd column
        [board[1], board[4], board[7]],
        # 3rd column
        [board[2], board[5], board[8]],
        # diagonals
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
        ]
    # each element in win_cases is a list of 3
    # if all 3 elements are X's or Y's a player (1 or 2) wins
    for i in win_cases:
        if i[0] == i[1] == i[2] == "X":
            print("Player 1 Wins!")
            return 1
        elif i[0] == i[1] == i[2] == "O":
            print("Player 2 Wins!")
            return 2
    return 0



# user play by entering the position number within the table
turn_count = 0
while game_status == 0:
    turn_count += 1
    # after the 9th turn the board is filled but with no winners
    if turn_count > 9:
        game_status = 3
        print("It's a draw")
        break
    # update board with every turn
    print_board()
    # player inputs position number they want to play
    player_input = input("Player's " + str(player_turn) + " Turn\n")
    if player_input not in board:
        print("Invalid Input, Please Try Again")
        break
    else:
        list_index = int(player_input) - 1
        if player_turn == 1:
            board[list_index] = "X"
            player_turn = 2
        elif player_turn == 2:
            board[list_index] = "O"
            player_turn = 1
    # if a player wins, game status changes and the loop breaks
    print()
    game_status = check_win()
print_board()