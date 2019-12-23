


# Tic-Tac-Toe Program using
# random number in Python

# importing all necessary libraries
import numpy as np
import random
from time import sleep

class TicTacToe:
    def __init__(self, board, current_state):
        self.board = board()
        self.current_state = current_state

    def get_current_state(self):
        return self.current_state

        # Creates an empty board
        def board():
            return(np.array([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]))

        # Check for empty places on board
        def board_fill(board):
            l = []

            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == 0:
                        l.append((i, j))
            return(l)

        # Select a random place for the player
        def random_place(board, player):
            selection = board_fill(board)
            current_loc = random.choice(selection)
            board[current_loc] = player
            return (board)

        # Checks whether the player has three
        # of their marks in a horizontal row

        def row_win(board, player):
            for r in range(len(board)):
                win = True

            for c in range(len(board)):
                if board[r, c] != player:
                    win = False
                    continue

            if win == True:
                return (win)
            return (win)

        # Checks whether the player has three
        # of their marks in a vertical row

        def col_win(board, player):
            for r in range(len(board)):
                win = True

            for c in range(len(board)):
                if board[c][r] != player:
                    win = False
                    continue

            if win == True:
                return (win)
            return (win)

        # Checks whether the player has three
        # of their marks in a diagonal row

        def diag_win(board, player):
            win = True

            for r in range(len(board)):
                if board[r, r] != player:
                    win = False
            return (win)

        # Evaluates specific state of current_state
        def current_state(X_WON, O_WON, DRAW, UNFINISHED):
            X_WON = False
            O_WON = False
            DRAW = False
            UNFINISHED = False


            for player in ['X', 'O']:
                if (row_win(board, player) or
                        col_win(board, player) or
                        diag_win(board, player)):
                    if player == 'X':
                        X_WON = True

                    else: O_WON = True


            if np.all(board != 0) and player not in ['X', 'O']:
                UNFINISHED = True
            else:
                DRAW = True

        # Main function to start the game
        def make_move():
            board, current_state, counter = board_fill(), 0, 1
            print(board)
            sleep(2)

            while get_current_state == 'UNFINISHED':
                for player in [X, O]:
                    board = random_place(board, player)
                    print("Board after " + str(counter) + " move")
                    print(board)
                    sleep(2)
                    counter += 1
                    current_state = current_state(board)

            return (current_state)

        # Driver Code
        print("Current state is: " + str(make_move()))