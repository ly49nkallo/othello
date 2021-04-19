# Othello

#### Video Demo:  https://youtu.be/IZt5yRIUUTw
#### Description:
This is my cs50 2020 final project.
This is based on the game "Othello", a special form of Reversi, read about Othello here: https://en.wikipedia.org/wiki/Reversi.
Othello is a board game that takes place on an 8x8 grid. Two players take turns placing pieces on the board until there are either no moves or tiles left.
Placing a piece will automatically convert any opponent pieces between your move and any of your pieces to your color. A valid move must convert at least one
other opponent piece.
Please visit the "instructions" in-game if you are still confused.

Link to github repo: https://github.com/ly49nkallo/othello

 ---

### Files:

There are two main files, runner.py and othello.py. 
Runner.py is in charge of handling the GUI related components through the module pygame (see requirements.txt). It also sorta acts like a state machine for my project, and is responsable for containing information about the current state that the entire program is in (ex. title screen, instructions screen, in-game, gameover, player-turn, ai-turn)


Othello.py is in charge of handling the game mechanics and data. Within Othello.py there is the Othello class, which is in charge of handeling one othello game session.
Whenever a new game of othello is started, a new instance of the Othello class is made. The othello class contains information about the current board layout, game states such as whether it is terminal and who the current player is. 
The othello class also contains the adversarial AI that you play against. I currently do not have a way for two players to compete, so my Othello is currently a strictly one person game. The AI is not, however, intellegent at all, as it relies on a list of all possible moves it can make and randomly indexes into that list to determine what move it makes, in otherwords, it is completely and utterly random. 
I have found this to work well, however, because othello is less dependent on strategy than other games. It is really hard to determine whether or not a current game state is in the favor of either player, as the winning player can change very frequently and suddenly. A random AI, therefore, is still very challenging to play against and it is not unlikely to be defeated by it. 

Code used in this project is heavily inspired or ported from code written for cs50ai 2020, specifically the implentation of tictactoe and minesweeper.
This is because Othello, too, is based on a grid like structure and requries the user to interact with each tile. 

To execute game, make sure you install requirements by entering:

> pip install -r requirements.txt

or install pygame directly by using:

> pip install pygame

Make sure you execute *runner.py* instead of *othello.py* to run game. To do this, run
> python runner.py

Ensure that *runner.py* and *othello.py* are in the same directory and that you are using python 3.0 or later.
If you have not already, I recommend using a Windows version of the python virtual environment to run this project.

#### NOTE: From my testing, it seems that a linux python virtual environment will NOT work because of some hardcode in runner.py, if you need to make a virtual environment, I recommend using Windows
Please report any bugs you find through github issues or through my email address, 
tyabrennan@gmail.com

I am already aware of a possible bug that may cause turns to be skipped under extreme circumstances but I have been unable to replicate the conditions in my own testing.

Thank you to cs50x!
Have fun!

Current build: Beta 1.0.0 v2
