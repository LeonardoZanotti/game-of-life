![](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)

# Game of life (Conways)
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

The “game” is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced “players”, by creating patterns with particular properties.

**How the game works**
Because the Game of Life is built on a grid of nine squares, every cell has eight neighboring cells, as shown in the given figure. A given cell (i, j) in the simulation is accessed on a grid [i][j], where i and j are the row and column indices, respectively. The value of a given cell at a given instant of time depends on the state of its neighbors at the previous time step. Conway’s Game of Life has four rules. 

* If a cell is ON and has fewer than two neighbors that are ON, it turns OFF.
* If a cell is ON and has either two or three neighbors that are ON, it remains ON.
* If a cell is ON and has more than three neighbors that are ON, it turns OFF.
* If a cell is OFF and has exactly three neighbors that are ON, it turns ON.

![](https://media.geeksforgeeks.org/wp-content/uploads/20201102133039/GameOfLifeDiagram.png)

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
