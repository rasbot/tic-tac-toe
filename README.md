# A Tic Tac Toe game in Python

<p align="center">
  <img src="https://raw.githubusercontent.com/rasbot/tic-tac-toe/master/images/tic-tac-toe.png" width="500" height="auto"/>
</p>

A simple game of tic tac toe, built in python. To run the game, clone or download the repo. Navigate to the main folder in the terminal, and run the game file with the command "python tic-tac-toe.py"

You will be asked to enter the names of the two players, and the program will pick one of the two as the first player. That player can choose to be X or O.

The board is visualized between moves, and looks like:
```
    BOARD
-------------
| O |   | X |
----+---+----
| X | X | O |
----+---+----
|   |   |   |
-------------
```
The players cannot place a letter on a non-empty space, and if the game is tied, the game will start over.

Next steps: 

* Hard code an AI to play against the player

* Use reinforcement learning to train an AI to learn from the player.