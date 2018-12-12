# Sudoku Solver

Solves any Sudoku puzzle using an efficient backtracking (depth-first) search algorithm. 

## Getting Started

Follow the steps below to solve any Sudoku board. 

### Prerequisites

Python 3.5.0+

### Clone the project

Clone the project to a local directory using either SSH:

```
git clone git@github.com:<github-username>/Sudoku-Solver.git
```
or using HTTPS:

```
git clone https://github.com/<github-username>/Sudoku-Solver.git
```

## Enter the Sudoku board to solve

In main.py, edit the `board` global variable to provide the unsolved Sudoku board. The `board` variable is a 2-deminsional array where the elements of the outer array are the rows of numbers, and elements in the inner arrays are numbers within a row. Use `0` for empty spaces on the Sudoku board.

Here is an example:

```
board = [[0,2,0,0,0,0,0,0,0],
         [0,0,0,6,0,0,0,0,3],
         [0,7,4,0,8,0,0,0,0],
         [0,0,0,0,0,3,0,0,2],
         [0,8,0,0,4,0,0,1,0],
         [6,0,0,5,0,0,0,0,0],
         [0,0,0,0,1,0,7,8,0],
         [5,0,0,0,0,9,0,0,0],
         [0,0,0,0,0,0,0,4,0]] 

#Note that cartesian position x,y on the Sudoku board (0,0 being on the top-left) is accessed by board[y][x]
```

### Running the program

To run the Sudoku Solver, navigate to the project directory on the command line and execute the following command:

```
python main.py
```

Here's the output for the board above:

```
Solving board:

0 2 0 0 0 0 0 0 0
0 0 0 6 0 0 0 0 3
0 7 4 0 8 0 0 0 0
0 0 0 0 0 3 0 0 2
0 8 0 0 4 0 0 1 0
6 0 0 5 0 0 0 0 0
0 0 0 0 1 0 7 8 0
5 0 0 0 0 9 0 0 0
0 0 0 0 0 0 0 4 0

Solved it!

1 2 6 4 3 7 9 5 8
8 9 5 6 2 1 4 7 3
3 7 4 9 8 5 1 2 6
4 5 7 1 9 3 8 6 2
9 8 3 2 4 6 5 1 7
6 1 2 5 7 8 3 9 4
2 6 9 3 1 4 7 8 5
5 4 8 7 6 9 2 3 1
7 3 1 8 5 2 6 4 9

Time to solve: 2.8038418292999268 seconds

```


## Authors

[Aziz Sonawalla](https://github.com/azizsonawalla)