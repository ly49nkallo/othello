
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

def other(player):
        if player == WHITE:
            return BLACK
        elif player == BLACK:
            return WHITE
        else:
            return None

class Othello():
    
    # controls all aspects of game session, including adversarial AI (not intellegent just random)

    def __init__(self):
        self.board = initial_state()
        self.c_player = WHITE
        self.theoretical_moves = set()
    
    def terminal(self):
        # test if the current board is a terminal state
        for tile in self.board:
            if tile == EMPTY:
                return False
        return True
    
    def player(self, board): #TODO: remove artifact
        # return current player to make move (assuming white goes first)
        return self.c_player
    
    def switch_player(self):
        if self.c_player == WHITE:
            self.c_player = BLACK
        elif self.c_player == BLACK:
            self.c_player = WHITE

    def get_surrounding_cells(self, cell):
        cells = set()
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < 8 and 0 <= j < 8:
                    cells.add((i, j))
                        
        return cells

    def update_moves(self, move):
        
        raise NotImplementedError

    def winner(self):  
        # return a string if you would be so nice (white or black)
        raise NotImplementedError
    
    def cascade(self, board, move, player):
        
        board = board.copy()
        marked = set()
        for dir in range(8):
            cursor = move
            tile = board[IX(cursor[0], cursor[1])]  # initialize
            possible = set()

            while True:
                
                # move the cursor
                if dir in (0,1,7): # move up
                    cursor = (cursor[0] - 1, cursor[1])
                if dir in {3,4,5}: # move down
                    cursor = (cursor[0] + 1, cursor[1])
                if dir in {1,2,3}: # move right
                    cursor = (cursor[0], cursor[1] + 1)
                if dir in {5,6,7}: # move left
                    cursor = (cursor[0], cursor[1] - 1)

                tile = board[IX(cursor[0], cursor[1])]
                if tile == EMPTY: # if raycast finds empty square
                    break
                if not tile == player:
                    possible.add(cursor)
                else:
                    if len(possible) > 0:
                        marked = marked.union(possible)
                    break
        print(marked)
        for cursor in marked:
            tile = board[IX(cursor[0], cursor[1])]
            if tile == WHITE:
                board[IX(cursor[0], cursor[1])] = BLACK
            if tile == BLACK:
                board[IX(cursor[0], cursor[1])] = WHITE
                

        return board, len(marked)
        
    def result(self, move):
        # non destructive board + move result

        board = self.cascade(self.board, move, self.player())
        board[IX(move[0], move[1])] = self.player(self.board)

        raise NotImplementedError
    
    def make_random_move(self):

        raise NotImplementedError
    
    def make_greedy_move(self):

        raise NotImplementedError
    
    def change_board(self, move):
        p = self.c_player
        self.board = self.cascade(self.board, move, p)[0]
        self.board[IX(move[0], move[1])] = p
        self.switch_player()
        

    
    #def make_move(self):


