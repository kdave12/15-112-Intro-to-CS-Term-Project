Krishna Dave, kdave
Recitation Section FF
Mentor: Chaya Wurman
readme.txt, Term Project

Term Project Name: Puzzle Mania

Puzzle Mania is a puzzle constructor and solver game. There are two main components of this game: 
1) The Solver
2) The Constructor (Jigsaw-type puzzle,  Grid puzzle)

My term project implements the module Python Imaging Library (PIL)
to crop images for the constructor, to detect outlines and colors of puzzle pieces 
using thresholding, for color/edge matching and checking the position of each piece 
on the final image for the solver.

PIL can be downloaded easily on any OS.
Here are the instructions: (Reference - Photo Manipulation, Optional Lecture Code)
Install PIL: (module for image manipulation)
1. Open terminal
2. type “sudo easy_install pip3” if not already installed
3. type “sudo pip3 install Pillow

To run my TP, it is essential to put the Term Project Python file in the same folder as 
the design documents folder. The design documents folder contains all the images used for
animation as well as images used for the solver and the constructor.

Detailed Description:

1) The Solver:  The first component of the game is called the solver, which solves an unsolved puzzle.
The program takes in a picture of unsolved shuffled puzzle pieces on a flat surface as well as a 
picture of the final puzzle image. It then returns the inputted image of the shuffled puzzle pieces
with numbers on the pieces in a consecutive order from a solved puzzle from left to right and top to bottom.
This feature is enabled due to thresholding to isolate the shuffled pieces, edge detection using the gradient 
difference between black and white colors, and finally color detection using pixel matching and average pixel 
present in each piece. 

2) The Constructor: The second part of this game is the constructor, which includes two main features: 
Puzzle and Grid.
 
Puzzle: The puzzle mode creates a jigsaw-type puzzle from an image, shuffles the pieces, 
	and asks the user to solve the puzzle. The user can pick from the existing picture library 
	or upload their own picture. The program will crop the image differently for each selected 
	difficulty level. For instance, low difficulty equates to a small number of big pieces with mostly
	same dimensions, medium level has medium sized pieces with different dimensions, 
	whereas high difficult corresponds to a high number of small pieces with diverse dimensions. 
	The puzzle pieces can be dragged and dropped using the mouse to the dashboard provided.

Grid:   The grid game is a different type of puzzle game. The program creates a grid puzzle from an image, 
	shuffles the pieces, and asks the user to solve the puzzle by switching two pieces. After the user
	selects two pieces, they are switched. The difficulty level varies based on the sizes of the pieces 
	and the extent to which the puzzle pieces can be moved. For the lowest difficulty, the pieces are
	relatively big and two pieces at any location can be switched. For the medium difficulty, the 
	pieces are small and two pieces at any location can be switched. For the highest difficulty level, 
	the puzzle pieces are small and can only be switched if they are adjacent. 
