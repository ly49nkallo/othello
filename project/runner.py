import pygame
import sys
import time

import othello as o


#Colors
black = (0, 0, 0)
green = (30, 150, 30)
white = (255, 255, 255)

# Create game
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# Set pygame window name
pygame.display.set_caption('Play Minesweeper!')

# Fonts
OPEN_SANS = "../assets/OpenSans-Regular.ttf"
UNIQUE = "../assets/Unique.ttf"
smallFont = pygame.font.Font(OPEN_SANS, 20)
mediumFont = pygame.font.Font(UNIQUE, 28)
largeFont = pygame.font.Font(UNIQUE, 40)

# Compute board size
BOARD_PADDING = 20
board_width = ((2 / 3) * width) - (BOARD_PADDING * 2)
board_height = height - (BOARD_PADDING * 2)
cell_size = int(min(board_width / 8, board_height / 8))
board_origin = (BOARD_PADDING, BOARD_PADDING)

game = o.Othello()
ai_turn = False

version = "Beta 1.0.0 v2"

user = None

Instructions = False

i = [
    "Take turns against the AI",
    "Make a move by clicking on an empty tile",
    "All pieces between your move and any other friendly piece will convert", 
    "Your move must convert at least one other tile",
    "Win by ending the game with the most pieces of your color on the board", 
    "The game ends when either all tiles are filled or no moves are left",
    "Black always starts first",
    "Find the repository for this project here: https://github.com/ly49nkallo/othello",
    "Find more on Othello here: https://en.wikipedia.org/wiki/Reversi",
    

]
if len(i) < 9:
    instructionSpacing = (height - 170)/len(i) - 10
else:
    instructionSpacing = (height - 170)/len(i) - 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(black)

    if Instructions:
        # https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
        title = largeFont.render("How to play", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Show instructions
        
        lineC = 0
        for line in i:
            lineC += 1
            text = smallFont.render(line, True, white)
            textRect = text.get_rect()
            textRect.center = ((width / 2), lineC * instructionSpacing + 100)
            screen.blit(text, textRect)
    
        exitButton = pygame.Rect((width / 2) - (width/12), height - 75, width/6, 40)
        exit = smallFont.render("Back", True, black)
        exitRect = exit.get_rect()
        exitRect.center = exitButton.center
        pygame.draw.rect(screen, white, exitButton)
        screen.blit(exit, exitRect)
        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if exitButton.collidepoint(mouse):
                time.sleep(0.2)
                Instructions = False

    elif user is None:
        title = largeFont.render("Play Othello", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        ver = smallFont.render(version, True, white)
        verRect = ver.get_rect()
        verRect.center = ((width / 2), height - 25)
        screen.blit(ver, verRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 16), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play white", True, black)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(6 * (width / 16), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play black", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        instructionsButton = pygame.Rect(11 * (width / 16), (height / 2), width/4, 50)
        instructions = mediumFont.render("Instructions", True, black)
        instructionRect = instructions.get_rect()
        instructionRect.center = instructionsButton.center
        pygame.draw.rect(screen, white, instructionsButton)
        screen.blit(instructions, instructionRect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = o.WHITE
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = o.BLACK
            elif instructionsButton.collidepoint(mouse):
                time.sleep(0.2)
                Instructions = True

    else:
        tile_size = 50
        tile_origin = (width / 2 - (4 * tile_size),
                       height / 2 - (4 * tile_size))
        collision_tiles = []
        for i in range(8):
            for j in range(8):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 5)
                pygame.draw.rect(screen, green, rect)

                # draw game pieces
                radius = 20
                board = game.board
                center = (
                    tile_origin[0] + j * tile_size + tile_size/2,
                    tile_origin[1] + i * tile_size + tile_size/2,
                )
                if board[o.IX(i, j)] == 1:
                    pygame.draw.circle(screen, black, center, radius)
                if board[o.IX(i, j)] == 2:
                    pygame.draw.circle(screen, white, center, radius)
                collision_tiles.append(rect)

        game_over = game.terminal
        player = game.player()

        if game_over:
            winner = game.winner()
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            if user == o.BLACK:
                title = "Play as black"
            else:
                title = "Play as white"
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = game.make_random_move()
                if game.change_board(move):
                    ai_turn = False
                else:
                    raise NameError("Somehow AI made invalid move!")
            else:
                ai_turn = True
        
        click, x, y = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(8):
                for j in range (8):
                    if game.board[o.IX(i, j)] == o.EMPTY and collision_tiles[o.IX(i, j)].collidepoint(mouse):
                        if not game.change_board((i, j)):
                            print("The move you made is not valid! Try again.")
                            time.sleep(0.1)
        
    pygame.display.flip()