
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
    
    def player(self, board):
        # return current player to make move (assuming white goes first)
        whiteCount = 0
        blackCount = 0
        for tile in board:
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
    
    def cascade(self, board, move):

        if not board[IX(move[0], move[1])] == EMPTY:
            raise NameError("cascading in occupied location", move, board[IX(move[0], move[1])])
        
        player = self.player(board)
        
        for dir in range(8):
            cursor = move
            tile = board[IX(cursor[0], cursor[1])]  # initialize
            while True:
                # move the cursor
                if dir in (0,1,7): # move up
                    cursor[0] -= 1
                if dir in {3,4,5}: # move down
                    cursor[0] += 1
                if dir in {1,2,3}: # move right
                    cursor[1] += 1
                if dir in {5,6,7}: # move left
                    cursor[1] -= 1
                
                tile = board[IX(cursor[0], cursor[1])]
                if tile == EMPTY:
                    break
                if not tile == player:
                    if tile == WHITE:
                        board[IX(cursor[0], cursor[1])] = BLACK
                    if tile == BLACK:
                        board[IX(cursor[0], cursor[1])] = WHITE
                else:
                    break
        
        
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

        self.board[IX(move[0], move[1])] = self.player(self.board)
        self.cascade(self.board, move)

    
    #def make_move(self):


