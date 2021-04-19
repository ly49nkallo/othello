import random as rand

EMPTY = None
BLACK = 1
WHITE = 2

def IX(i, j):
    # Use this to index into game board
    if i not in range(8) or j not in range(8):
        print("fish mk.2")
    return (j + (i * 8))

def initial_state():

    # the starting posistion of every new othello game

    b = [EMPTY] * (8 * 8)  # we use a one dimentional array because it is theoretically faster (and I feel like it)
    b[IX(3,3)] = WHITE
    b[IX(4,4)] = WHITE
    b[IX(3,4)] = BLACK
    b[IX(4,3)] = BLACK

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
        self.c_player = BLACK
        self.moves = set()
        self.terminal = False
        self.update_moves()
        rand.seed(a=None, version=2)
        
    
    def isTerminal(self):
        # test if the current board is a terminal state
        self.update_moves()
        if self.moves == set():
            return True
        player = self.player()
        player_moves = set()
        for move in self.moves:
            if self.cascade(self.board, move, player)[1] > 0:
                
                player_moves.add(move)
        return not len(player_moves)
    
    def player(self):
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

                if 0 <= i < 8 and 0 <= j < 8:
                    cells.add((i, j))
                        
        return cells

    def update_moves(self):
        self.moves = set()
        for i in range(8):
            for j in range(8):
                v = self.board[IX(i,j)]
                c = set()
                for cell in self.get_surrounding_cells((i,j)):
                    c.add(self.board[IX(cell[0], cell[1])])
                if v == EMPTY and any(c):
                    self.moves.add((i,j))

    def winner(self):  
        # return a string if you would be so nice (white or black)
        whiteCount = 0
        blackCount = 0
        for cell in self.board:
            if cell == WHITE:
                whiteCount += 1
            elif cell == BLACK:
                blackCount += 1
        if whiteCount == blackCount:
            return None
        if whiteCount > blackCount:
            return "White"
        else:
            return "Black"

        raise Exception
    
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
                
                if cursor[0] not in range(8) or cursor[1] not in range(8):
                    break
                try:
                    tile = board[IX(cursor[0], cursor[1])]
                except IndexError:
                    print("fish")
                    tile = EMPTY
                if tile == EMPTY: # if raycast finds empty square
                    break
                if not tile == player:
                    possible.add(cursor)
                else:
                    if len(possible) > 0:
                        marked = marked.union(possible)
                    break
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
        board[IX(move[0], move[1])] = self.player()

        raise NotImplementedError
    
    def make_random_move(self):
        
        x = list()
        player = self.player()
        for move in self.moves:
            if self.cascade(self.board, move, player)[1]:
                x.append(move)
        try:
            choice = rand.choice(x)
        except IndexError:
            raise NameError("no more moves remain")
        return choice 
    
    def make_greedy_move(self):

        raise NotImplementedError

    def change_board(self, move):
        if move not in self.moves:
            raise NameError("move is not valid 147")
        p = self.c_player
        c = self.cascade(self.board, move, p)
        if c[1] > 0: 
            self.board = c[0]
            self.board[IX(move[0], move[1])] = p
            self.update_moves()
            self.switch_player()
        else:
            return False
        self.terminal = self.isTerminal()
        return True
        

    
    #def make_move(self):


