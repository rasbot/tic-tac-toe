"""A Tic Tac Toe game!"""
import random
import numpy as np


def update_board(coords=None, letter=None, update_coord=None, valid=True, reset=False):
    """
    Updates the player board, or resets it depending on the value of the reset bool

            Parameters:
                   coords (nested list): Coordinates array
                   letter (str): Which letter to place on the board (X or O)
                   update_coord (list): Which coordinates to update with letter
                   valid (bool): Used to determine if the update_coord is
                           clear or has a X or O already in play
                   reset (bool): True to clear board

            Returns:
                    coords (nested list) - Updated board coordinates
                    board (str) - Visualization of board
                    valid (bool) - Keep track of if the move is valid
    """
    if reset:
        coords = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    else:
        coords[update_coord[0]-1][update_coord[1]-1] = letter
        valid = True
    board = f"""    BOARD
-------------
| {coords[0][0]} | {coords[0][1]} | {coords[0][2]} |
-------------
| {coords[1][0]} | {coords[1][1]} | {coords[1][2]} |
-------------
| {coords[2][0]} | {coords[2][1]} | {coords[2][2]} |
-------------"""
    return coords, board, valid


def change_player(players, player_int):
    """
    Swaps the player.

            Parameters:
                    players (list): A list of strings with both player names
                    player_int (int): Int that is either positive or negative

            Returns:
                    player (str): The name of the current player
                    player_int (int): Keep track of the player int
    """
    player_int *= -1
    if player_int > 0:
        player = players[0]
    else:
        player = players[1]
    return player, player_int


def one_round(coords, player, player_int, won, valid, d, players):
    """
    Play one round. Read player coordinates for next move, update the board,
    check for a winner, and if no winner, swap players

            Parameters:
                    coords (nested list): Coordinates array
                    player (str): The name of the current player
                    player_int (int): Int that is either positive or negative
                    won (bool): Has either player won?
                    valid (bool): Keep track of if the move is valid
                    d (dict): Dictionary of player names / letters
                    players (list): List of players

            Returns:
                    player (str): The name of the current player
                    player_int (int): Int that is either positive or negative
                    won (bool): Has either player won?
                    winner (str): Which player (X or O) is a winner?
    """
    winner = ''
    while True:
        move = input(f"{player}, pick your coordinates: ")
        move_coords = [int(move[0]), int(move[2])]
        if move_coords[0] < 1 or move_coords[0] > 3 or move_coords[1] < 1 or move_coords[1] > 3:
            print("Invalid coordinates, pick again!")
            valid = False
        elif coords[move_coords[0]-1][move_coords[1]-1] != " ":
            print("Board position already taken. Please pick again!")
            valid = False
        else:
            valid = True
        if valid:
            coords, board, valid = update_board(coords, d[player], move_coords)
            break

    print(board)

    filled_row_count = 0
    for row in coords:
        if " " not in row:
            filled_row_count += 1
    if filled_row_count == 3:
        print("There are no more moves. The game is a tie. Please play again!")
        play_game()
    if check_winner(coords) != False:
        won = True
        winner = check_winner(coords)
    player, player_int = change_player(players, player_int)
    return player, player_int, won, winner


def check_row(row):
    """
    Checks a row (list) to see if all values are equal and not empty strings

            Parameters:
                    row (list): A list of strings, either " ", "X", or "O"

            Returns:
                    row[0] (str): The non-empty string of the winning letter
                    False (bool): If the row is not a winner, return False
    """
    if len(set(row)) == 1 and row[0] != " ":
        return row[0]
    else:
        return False


def check_winner(coords):
    """
    Checks if there is a winner on the board

            Parameters:
                    coords (nested list): Coordinates array

            Returns:
                    winner (str): Which player (X or O) is a winner?
    """
    winner = ''
    # checks rows
    for i in range(3):
        res = check_row(coords[i])
        if res != False:
            winner = res
            break

    # checks columns
    for i in range(3):
        res = check_row([coords[j][i] for j in range(len(coords))])
        if res != False:
            winner = res
            break

    # checks diagonals
    arr = np.array(coords)
    res = check_row(list(np.diagonal(np.fliplr(arr))))
    if res != False:
        winner = res
    res = check_row(list(arr.diagonal()))
    if res != False:
        winner = res
    if winner == '':
        return False
    else:
        return winner


def play_game():
    """
    Run the game. Will initialize the game board, allow players to pick their
    names and letters (X or O), give a quick tutorial on how to place their moves,
    and proceed with the logic to run the game.
    """
    coords = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    coords, board, valid = update_board(reset=True)

    player_1_name = input("Player 1, enter your name: ")

    while True:
        player_2_name = input("Player 2, enter your name: ")
        if player_2_name == player_1_name:
            print("You cannot have the same name as player 1. Please pick a different name!")
        else:
            break

    players = [player_1_name, player_2_name]

    first = random.choice(players)

    if first == player_2_name:
        players = [player_2_name, player_1_name]

    player_int = 1
    player = first
    won = False
    valid_xo = False

    while valid_xo == False:
        first_val = input(f"{first} will go first. {first}, pick either X or O: ")
        if first_val == 'X':
            second_val = 'O'
            valid_xo = True
        elif first_val == 'O':
            second_val = 'X'
            valid_xo = True
        else:
            print("Please pick a valid choice of either X or O")

    d = {players[0]: first_val, players[1]: second_val}

    print(f"""
    The player board looks like:

    {board}
    """)
    coords, board, valid = update_board(coords, 'X', [2, 1])
    print(f"""You will enter your coordinates as row, column...such as: 2, 1
    for the second row, first column...which will look like:

    {board}""")
    coords, board, valid = update_board(reset=True)

    while won == False:
        player, player_int, won, winner = one_round(
            coords, player, player_int, won, valid, d, players)
    for k, v in d.items():
        if v == winner:
            print(f"Winner! Player {k} is victorious!")

    choice = input("Play again? y/n: ")
    if choice in ('y', 'Y'):
        play_game()
    else:
        print("Thank you for playing!")


if __name__ == "__main__":
    play_game()
