import random


class TicTacToe:
    """TicTacToe class. Create an instance of this class to play an amazing game
    of tic-tac-toe!"""
    def __init__(self):
        """Initialize the board dict and valid coordinates."""
        self.board_dict = {
            1: " ",
            2: " ",
            3: " ",
            4: " ",
            5: " ",
            6: " ",
            7: " ",
            8: " ",
            9: " ",
        }
        self.valid_coords = list("123456789")
        self.board = None
        self.current_player = None
        self.players = None

    @staticmethod
    def get_enter_prompt(text: str) -> str:
        """Return an input prompt which will be displayed if the user is bad at
        following directions.

        Args:
            text (str): Text to inject into the f-string.

        Returns:
            str: Randomized cheeky response.
        """
        input_prompts = [
            f"Please hit {text} to continue...",
            f"You need to actually hit {text} if you want to play!",
            f"Try hitting {text} ...",
            f"You will not move on from this prompt unless you hit {text}! Try again.",
            "Just hit the correct key, this is not that difficult...",
            f"OK, now actually hit {text} to continue!",
        ]
        return random.choice(input_prompts)

    def update_board_dict(self, coord: int = None, move: str = None) -> None:
        """Update the board_dict with 'X' or 'O' for the coord specified.

        Args:
            coord (int, optional): Coordinate of the board (nums 1-9). Defaults to None.
            move (str, optional): Player move (X or O). Defaults to None.
        """
        if move:
            self.board_dict[coord] = move

    def update_board(self) -> None:
        """Update the player board which is printed to the console."""
        self.board = f"""    BOARD
-------------
| {self.board_dict[7]} | {self.board_dict[8]} | {self.board_dict[9]} |
----+---+----
| {self.board_dict[4]} | {self.board_dict[5]} | {self.board_dict[6]} |
----+---+----
| {self.board_dict[1]} | {self.board_dict[2]} | {self.board_dict[3]} |
-------------"""

    def get_player_move(self) -> int:
        """Get the coordinate of the player move. If the player enters
        an invalid selection (not a number 1-9) or a selection that is already
        occupied by a previous move, they will be asked to pick another move.

        Returns:
            int: Coordinate of the player move.
        """
        is_valid_move = False
        while is_valid_move is False:
            coord = input(
                f"What is your move {self.players[self.current_player]['name']}? "
            )
            if coord in self.valid_coords:
                player_coord = int(coord)
                is_valid_move = True
                self.valid_coords.remove(coord)
            else:
                print(
                    "Please pick a valid move (number keys 1-9) that has not been played..."
                )
        return player_coord

    def update_from_player_move(self, player_coord: int) -> None:
        """Update the board_dict and player board with the current player's move.

        Args:
            player_coord (int): Player coordinate of the current move.
        """
        self.update_board_dict(player_coord, self.players[self.current_player]["move"])
        self.update_board()
        print(f"\n{self.board}\n")

    def change_player(self) -> None:
        """Swap the numeric value (0 or 1) of the current player."""
        self.current_player = 1 - self.current_player

    def get_player_info(self) -> None:
        """Get the player info for both players. This will store the player
        names and their move (X or O) to a class variable dict. The randomly selected
        current player numeric value (0 or 1) will be stored in a
        class variable 'current_player'
        """
        player_1_name = input("\nPlayer 1, enter your name: ")

        while True:
            player_2_name = input("Player 2, enter your name: ")
            if player_2_name == player_1_name:
                print(
                    "You cannot have the same name as player 1. Please pick a different name!"
                )
            else:
                break

        self.players = {
            0: {"name": player_1_name, "move": ""},
            1: {"name": player_2_name, "move": ""},
        }

        self.current_player = random.choice(list(self.players.keys()))
        is_valid_xo = False

        while is_valid_xo is False:
            first_val = input(
                f"{self.players[self.current_player]['name']} will go first. \
                {self.players[self.current_player]['name']}, pick either X or O: "
            )
            if first_val in ("X", "x"):
                second_val = "O"
                is_valid_xo = True
            elif first_val in ("O", "o"):
                second_val = "X"
                is_valid_xo = True
            else:
                print(self.get_enter_prompt("'X' or 'O'"))
        first_val = first_val.upper()
        self.players[self.current_player]["move"] = first_val
        self.players[1 - self.current_player]["move"] = second_val

    def is_player_winner(self) -> bool:
        """Check if the current player has a secured a win with their
        most recent move.

        Returns:
            bool: True if the player has just won the game, False if not.
        """
        winning_coords = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]
        player_move = self.players[self.current_player]["move"]
        player_coords = []
        for coord, move in self.board_dict.items():
            if move == player_move:
                player_coords.append(coord)
        for i in winning_coords:
            if set(i).issubset(player_coords):
                return True
        return False

    def is_draw(self) -> bool:
        """Check if there are any moves left on the board.

        Returns:
            bool: True if there are no more valid moves left.
        """
        return len(self.valid_coords) == 0

    def player_move_if_no_win(self) -> bool:
        """Complete a player move by getting the player move from the
        console, updating the board_dict, and check if the player has
        won. If not, switch players.

        Returns:
            bool: True if the last move is a win, False if no winner.
        """
        player_coord = self.get_player_move()
        self.update_from_player_move(player_coord)
        if self.is_player_winner():
            print(
                f"Congratulations {self.players[self.current_player]['name']}, you won!"
            )
            return True
        if self.is_draw():
            print("No more valid moves left on the board. The game is a draw!")
        self.change_player()
        return False

    def show_game_rules(self):
        """Text rules that explain how to play the game."""
        print(f"\n\t{'*'*10}Let's play Tic-Tac-Toe!{'*'*10}\n")
        print(
            """After both players enter their name, one player will be chosen at random
to start the game. That player will chose to be 'X' or 'O'. \n
The board will be shown after each move. \n
To play your turn, type the number that corresponds to the position
of the board as it looks on the 10 key representation on a keyboard, which
looks like:"""
        )
        print(
            """\n    BOARD
-------------
| 7 | 8 | 9 |
----+---+----
| 4 | 5 | 6 |
----+---+----
| 1 | 2 | 3 |
-------------\n"""
        )

        entry = input("OK, hit enter to start!")
        while entry:
            entry = input(self.get_enter_prompt("the enter key"))


def play_game():
    """
    Run the game. Will initialize the game board, allow players to pick their
    names and letters (X or O), and run the game.
    """
    is_winner = False
    tic_tac_toe_game = TicTacToe()
    tic_tac_toe_game.show_game_rules()
    tic_tac_toe_game.get_player_info()
    while not is_winner:
        is_winner = tic_tac_toe_game.player_move_if_no_win()
    choice = input("Play again? y/n: ")
    if choice in ("y", "Y"):
        play_game()
    else:
        print("Thank you for playing!")


if __name__ == "__main__":
    play_game()
