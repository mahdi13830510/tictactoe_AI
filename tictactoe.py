"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # In initial game state, X plays first
    if sum(row.count(EMPTY) for row in board) == 9:
        return X
    
    # If X symbols are more or equal to O symbols, X plays
    elif sum(row.count(X) for row in board) <= sum(row.count(O) for row in board):
        return X
    
    # If X symbols are less then O symbols, O plays
    elif sum(row.count(X) for row in board) > sum(row.count(O) for row in board):
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in board:
        for col in row:
            if col == EMPTY:
                actions.add((board.index(row), row.index(col)))
    
    return actions
                


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = copy.deepcopy(board)
    if player(new_board) == X:
        new_board[i][j] = X
    
    elif player(new_board) == O:
        new_board[i][j] = O
    
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    """# Check rows for win
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    # Check columns for win
    for col in range(3):
        if all(row[col] == X for row in board):
            return X
        if all(row[col] == O for row in board):
            return O"""
    
    # Check diagonals for win   
    """
    if all(board[i][i] for i in range(3)) == X:
        return X
    if all(board[i][2-i] for i in range(3)) == X:
        return X
    if all(board[i][i] for i in range(3)) == O:
        return O
    if all(board[i][2-i] for i in range(3)) == O:
        return O
    else:
        return None
    """
    # Check rows
    for row in board:
        if row.count('X') == 3:
            return 'X'
        if row.count('O') == 3:
            return 'O'
            
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0] 
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
        
    # No winner 
    return None
    
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win is None:
        return False
    return True if ((win) or (sum(row.count(EMPTY) for row in board) == 0)) else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v
    
    
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action))) 
        return v
    

    return max(actions(board), key=lambda x: min_value(result(board, x)))

