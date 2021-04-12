
EMPTY = None
BLACK = 1
WHITE = 2

def IX(i, j):
    # Use this to index into game board
    return (j + (i * 8))

def initial_state():

    # the starting posistion of every new othello game

    b = [EMPTY] * (8 * 8)  # we use a one dimentional array because it is theoretically faster (and I feel like it)
    b[IX(3,3)] = BLACK
    b[IX(4,4)] = BLACK
    b[IX(3,4)] = WHITE
    b[IX(4,3)] = WHITE
    return b

class Othello():
    
    # controls all aspects of game session, including adversarial AI (not intellegent just random)

    def __init__(self):
        self.board = initial_state()
    
    def terminal(self):
        # test if the current board is a terminal state
        for tile in self.board:
            if tile == EMPTY:
                return False
        return True
    
    def player(self):
        # return current player to make move (assuming white goes first)
        whiteCount = 0
        blackCount = 0
        for tile in self.board:
            if tile == BLACK:
                blackCount += 1
            if tile == WHITE:
                whiteCount += 1

        if whiteCount == blackCount:
            return WHITE
        else:
            return BLACK

    def winner(self):  
        # return a string if you would be so nice (white or black)
        raise NotImplementedError
    
    def result(self, move):
        # non destructive board + move result
        board = self.board.copy()
        board[IX(move[0], move[1])] = self.player()
        return board

        raise NotImplementedError
    
    def make_random_move(self):

        raise NotImplementedError
    
    def make_greedy_move(self):

        raise NotImplementedError
    
    def change_board(self, move):

        self.board[IX(move[0], move[1])] = self.player()

    
    #def make_move(self):


