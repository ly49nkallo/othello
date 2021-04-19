# Othello

#### Video Demo:  https://youtu.be/97_3Qfey1Hc
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
Runner.py is in charge of handling the GUI related components through the module pygame (see requirements.txt).
Othello.py is in charge of handling the game mechanics and data. There are also two python virtual environments,
one for Windows and the other is for Linux. I do not recommend using these virtual environments on your own machine however.

Code used in this project is heavily inspired or ported from code written for cs50ai 2020

To execute game, make sure you install requirements by entering:

> pip install -r requirements.txt

or install pygame directly by using:

> pip install pygame

Make sure you execute *runner.py* instead of *othello.py* to run game. To do this, run
> python runner.py

Ensure that *runner.py* and *othello.py* are in the same directory and that you are using python 3.0 or later.
If you have not already, I recommend using a Windows version of the python virtual environment to run this project.

Please report any bugs you find through github issues or through my email address, tyabrennan@gmail.com

Thank you to cs50x!
Have fun!

Current build: Beta 1.0.0 v2
