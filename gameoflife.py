#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/game-of-life

# -*- coding: utf-8 -*-
import sys,os,platform
from optparse import OptionParser
import numpy as np
from matplotlib import pylab
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pylab import *
from math import *

##### colors
colors = True	# output colored c:
machine = sys.platform 		# detecting the os
checkPlatform = platform.platform()	# get current version of os
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False 	# Mac and Windows shouldn't display colors :c
if checkPlatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    color = True	# coooolorssss \o/
    os.system('')	# Enables the ANSI -> standard encoding that reads that colors
if not colors:
    BGreen = BYellow = BPurple = BCyan = Yellow = Green = Red = Blue = On_Black = ''
else:
    BGreen = "\033[1;32m"     # Bold Green
    BYellow = "\033[1;33m"    # Bold Yellow
    BPurple = "\033[1;35m"    # Bold Purple
    BCyan = "\033[1;36m"      # Bold Cyan
    Yellow = "\033[0;33m"     # Yellow
    Green = "\033[0;32m"      # Green
    Red = "\033[0;1"      # Red
    Blue = "\033[0;34m"     # Blue

    # Background
    On_Black="\033[40m"       # Black Background

def main():
    args = sys.argv
    ##### logo
    if len(args) == 1:		### Made with figlet or toilet
        print('''
            {On_Black}{BCyan}
            \t  ____                               __   _     _  __      
            \t / ___| __ _ _ __ ___   ___    ___  / _| | |   (_)/ _| ___ 
            \t| |  _ / _` | '_ ` _ \ / _ \  / _ \| |_  | |   | | |_ / _ \\
            \t| |_| | (_| | | | | | |  __/ | (_) |  _| | |___| |  _|  __/
            \t \____|\__,_|_| |_| |_|\___|  \___/|_|   |_____|_|_|  \___|
            \t
            {BYellow} # Zanotti's python Game of life{Green}
            https://github.com/LeonardoZanotti/game-of-life

    For {BGreen}help {Green}type:
    \t
    {BGreen}$ python3.7 gameoflife.py --help                             
            '''.format(BCyan=BCyan,BGreen=BGreen,Green=Green,BYellow=BYellow,On_Black=On_Black))     

    ##### options list
    parser = OptionParser(add_help_option=False)
    parser.add_option('-h','--help',action='store_true',dest='help')
    parser.add_option('-t','--template',action='store_true',dest='template')
    opts, args = parser.parse_args()

    ##### analysing options
    if (opts.help or len(args) <= 1):
        helper()                              

    if len(args) > 0:
        fig, ax = plt.subplots()
        square_size = 1
        n_rows = n_columns = int(args[0])
        random = False if opts.template else True
        checkerboard = make_checkerboard(n_rows, n_columns, square_size, random)
        saveCheckerboard(checkerboard)
        animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 10, 0.1), fargs=(checkerboard, ), interval=200)
        plt.show()

    sys.exit()

savedCheckerboard = None
def saveCheckerboard(checkerboard):
    global savedCheckerboard
    savedCheckerboard = checkerboard

def animation_frame(i, checkerboard):
    global savedCheckerboard
    if i > 5:
        sys.exit()
    updatedCheckerboard = updateCheckerboard(savedCheckerboard)
    plt.imshow(updatedCheckerboard)
    return updatedCheckerboard 

def updateCheckerboard(checkerboard):
    if (checkerboard[0][0] == 1.0):
        checkerboard[0][0] = 0.0
    else:
        checkerboard[0][0] = 1.0
    # checkerboard[0][0] = 1.0 if 0.0 else 0.0
    saveCheckerboard(checkerboard)
    print(checkerboard[0][0])
    return checkerboard

##### options help
def helper():
    print('''
{BGreen}Usage: gameoflife.py [size of the canvas]

Example: python3.7 gameoflife.py 255
This will create a canvas of 255x255 random cells

Example: python3.7 gameoflife.py 255 --template
This will create a canvas of 255x255 cells from a defined template
    '''.format(BGreen=BGreen))
    return

def make_checkerboard(n_rows, n_columns, square_size, random):
    # print('Making checkearboard...')
    new_rows = n_rows if random else 21
    new_columns = n_columns if random else 49
    if (random):
        rows_grid, columns_grid = np.meshgrid(range(new_rows), range(new_columns), indexing='ij')
        # print('Grids done')
        # print('Rows:')
        # print(rows_grid)
        # print('Colums')
        # print(columns_grid)

        r = new_rows
        c = new_columns
        p = 0.4
        high_res_checkerboard = np.random.choice(a=[False, True], size=(r, c), p=[p, 1-p])
    else:
        template = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        # print('Template:')
        # print(template)
        high_res_checkerboard = np.array(template, dtype=bool)

    # print('Checkeds:')
    # print(high_res_checkerboard)

    square = np.ones((square_size,square_size))
    # print('Square size:')
    # print(square)

    checkerboard = np.kron(high_res_checkerboard, square)[:new_rows,:new_columns]
    # print('Checkerboard:')
    # print(checkerboard)

    return checkerboard

if __name__ == '__main__':
    main()