Python Tic-Tac-Toe Game (2V2)
-------------------------------------------------------
This repository contains a classic Tic-Tac-Toe game implemented in Python, designed for 2 players to play against each other. Challenge your strategic thinking against your friend in this timeless grid-based game!


Description
---------------------------------------------------------
This project brings the classic Tic-Tac-Toe game to life, allowing 2 players to test each other's skills against an artificial intelligence opponent. The game is played on a 3x3 grid, where players take turns marking spaces with their symbol (typically 'X' for player 1 and 'O' for player 2). The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game. If all nine squares are filled and no player has three marks in a row, the game is a draw.

Features
-----------------------------------
  - Classic 3x3 Tic-Tac-Toe gameplay.
  - 2-player mode against each other.
  - Clear turn-based interaction.
  - Win, lose, and draw conditions detection.
  - Simple console-based interface.

Prerequisites
-----------------------------
To run this game, you will need:
  - Python 3.13.5

Installation
----------------------------------
1. Install all the necessary libraries if not already installed

        pip install tkinter copy
   
3. Run the game - Navigate to the directory where you cloned the repository (or saved the tic_tac_toe.py file) and run the script:

        python tic_tac_toe.py

How to Play
--------------------
**Objective - ** The goal is to be the first to get three of your marks ('X' or 'O') in a horizontal, vertical, or diagonal row.

**Controls - ** The game will prompt you to enter a number from 1 to 9 to choose your move. Each number corresponds to a position on the 3x3 board:

    1 | 2 | 3
    --+---+--
    4 | 5 | 6
    --+---+--
    7 | 8 | 9

  - Follow the on-screen prompts to make your move.

Game Mechanics
---------------------------------
  - Player 1 Turn: Player 1 typically goes first, marking 'X'.
  - Player 2 Turn: After Player 1 makes a move, Player 2 makes its move, marking 'O'.
  - Winning Condition: A player wins if they successfully place three of their marks in a straight line (horizontal, vertical, or diagonal).
  - Draw Condition: If all nine squares are filled and neither player has achieved a winning line, the game is a draw.
  - Game End: The game concludes when a win or draw condition is met. You can re-run the script to play a new game.

Code Structure
----------------------------------------
  - The game is primarily implemented in a 2-player Python script (e.g., tic_tac_toe.py). Key components typically include:
  - Board Representation: A data structure (e.g., a list or array) to represent the 3x3 game board.
  - Display Function: A function to print the current state of the board to the console.
  - Player Input Handling: Logic to receive and validate the human player's moves.   
  - Win/Draw Check: Functions to determine if a win condition has been met or if the game is a draw.
  - Game Loop: The main loop that manages turns, updates the board, checks for game end conditions, and displays messages.

Contributing
---------------
You can fix this repository by opening issues and submitting pull requests.

License
---------------
This project is open-source and available under the MIT License.

**Enjoy challenging your friends in Tic-Tac-Toe!**
