![](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)

# Game of life (Conways)
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine. 

## Running this game
First of all, you will need [Python 3.7+](https://www.python.org/).
With this, is needed to install the requirements of this project: [Numpy](https://numpy.org) and [Matplotlib](https://matplotlib.org/). To install it, just run:
```bash
$ python -m pip install numpy matplotlib
```
All installed, you can run the project helper with:
```bash
$ python gameoflife.py --help
```
This will give you an example of how to use the project.

Basically, you can run the project in a random mode, generating a NxN board with a random start configuration or you can use "--template" to see the [Gosper glider gun](https://conwaylife.com/wiki/Gosper_glider_gun).

## Acknowledgment
Thanks to this [Geeks for Geeks article](https://www.geeksforgeeks.org/conways-game-life-python-implementation/), improved by ganesh_kavhar. It give me the inspiration to do my own version of the game.

## Leonardo Zanotti
