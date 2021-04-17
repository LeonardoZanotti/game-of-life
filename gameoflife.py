#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/Zawnbe

# pytube documentation if you are reading this to learn :D
# https://readthedocs.org/projects/python-pytube/downloads/pdf/latest/

# -*- coding: utf-8 -*-
import sys,os,platform
from optparse import OptionParser
import numpy as np
from matplotlib import pylab
import matplotlib.pyplot as plt
from pylab import *
from math import *

args = sys.argv

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
	Red = "\033[0;31m"      # Red
	Blue = "\033[0;34m"     # Blue

	# Background
	On_Black="\033[40m"       # Black Background

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

	sys.exit()

##### options help
def helper():
	print('''
{BGreen}Usage: gameoflife.py [size of the canvas] [cells initially alive]

Example: python3.7 gameoflife.py 255 1 2 3 4 8 9
This will create a canvas of 255x255 cells with the cells 1, 2, 3, 4, 8 and 9 initially alive
	'''.format(BGreen=BGreen))
	return

##### options list
parser = OptionParser(add_help_option=False)
parser.add_option('-h','--help',action='store_true',dest='help')
opts, args = parser.parse_args()

##### analysing options
if (opts.help or len(args) <= 1):
	helper()

def make_checkerboard(n_rows, n_columns, square_size):
    rows_grid, columns_grid = np.meshgrid(range(n_rows), range(n_columns), indexing='ij')
    print(rows_grid)
    print(columns_grid)
    high_res_checkerboard = np.mod(rows_grid, 2) + np.mod(columns_grid, 2) == 1
    print(high_res_checkerboard)
    square = np.ones((square_size,square_size))
    print(square)
    checkerboard = np.kron(high_res_checkerboard, square)[:n_rows,:n_columns]
    return checkerboard

if (args[0]):
    square_size = 5
    n_rows = 14
    n_columns = 67
    checkerboard = make_checkerboard(n_rows, n_columns, square_size)
    print(checkerboard)
    plt.imshow(checkerboard)
    plt.show()

if len(args) > 1:
    print('dale')

sys.exit()