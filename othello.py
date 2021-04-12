
EMPTY = None
BLACK = 1
WHITE = 2

def IX(i, j):
    # Use this to index into game board
    return (i + (j * 8))

def initial_state():
    # the starting posistion of every new othello game
    b = [EMPTY] * (8 * 8)
    b[IX(3,3)] = BLACK
    b[IX(4,4)] = BLACK
    b[IX(3,4)] = WHITE
    b[IX(4,3)] = WHITE
    return b



