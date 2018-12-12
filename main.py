import math
import time
import sys
import click
import os
from copy import deepcopy, copy

# Global variable to store Sudoku board to solve
# Note that cartesian position x,y on the Sudoku board (0,0 being on the top-left) is accessed by board[y][x]
board = [[]]

def parseTextFile(path):
	"""
	Parses .txt file on given path and insantiates the global
	variable board as a 2D array.
	"""
	file = open(path, 'r')
	global board
	board = []
	for line in file:
		line = line.strip('\n').replace(' ', '')
		if len(line) != 9:
			print("Invalid Sudoku board provided")
			return
		row = []
		for character in line:
			row.append(int(character))
		board.append(row)


def inclusive_range(start, end):
	"""
	Returns range that includes both start and end numbers
	"""
	return range(start, end+1)


def findNumbersInBox(x, y, board):
	"""
	Returns all numbers in the Sudoku box of given position,
	except the number in the position itself.
	"""
	boxNum = math.floor(x/3) + 3*(math.floor(y/3))
	
	if (boxNum == 0 or boxNum == 3 or boxNum == 6):
		x_min = 0
	if (boxNum == 1 or boxNum == 4 or boxNum == 7):
		x_min = 3
	if (boxNum == 2 or boxNum == 5 or boxNum == 8):
		x_min = 6

	if (boxNum == 0 or boxNum == 1 or boxNum == 2):
		y_min = 0
	if (boxNum == 3 or boxNum == 4 or boxNum == 5):
		y_min = 3
	if (boxNum == 6 or boxNum == 7 or boxNum == 8):
		y_min = 6

	nums = []
	for i in inclusive_range(x_min, x_min+2):
		for j in inclusive_range(y_min, y_min+2):
			if not (j == y and i == x):
				nums.append(board[j][i])

	return nums


def findNumbersInRow(x, y, board):
	"""
	Returns all numbers in the row of given position,
	except the number in the position itself.
	"""
	nums = []
	for i in inclusive_range(0,8):
		if i==x:
			continue
		nums.append(board[y][i])
	return nums


def findNumbersInCol(x, y, board):
	"""
	Returns all numbers in the col of given position,
	except the number in the position itself.
	"""
	nums = []
	for i in inclusive_range(0,8):
		if i==y:
			continue
		nums.append(board[i][x])
	return nums


def isValidInPosition(x, y, num, board):
	"""
	Returns true if number can be legally placed
	in given position
	"""
	if num > 9:
		return False
	
	if num < 1:
		return False
	
	if num in findNumbersInCol(x,y,board):
		return False
	
	if num in findNumbersInRow(x,y,board):
		return False
	
	if num in findNumbersInBox(x,y,board):
		return False

	return True


def findPrevEmptyPosition(x,y):
	"""
	Returns previous position [x_prev,y_prev] to given position
	that was not originally filled
	"""
	
	if (x == 0 and y == 0):
		x_prev = 0
		y_prev = 0
		return [-1,-1]

	if x == 0:
		x_prev = 8
		y_prev = y-1
	else:
		x_prev = x-1
		y_prev = y

	if board[y_prev][x_prev] == 0:
		return [x_prev, y_prev]
	else:
		return findPrevEmptyPosition(x_prev,y_prev)



def printBoard(boardToPrint):
	"""
	Prints the given sudoku board
	"""
	printOut = ""

	for row in boardToPrint:
		for num in row:
			printOut += str(num) + " "
		printOut += "\n"

	print(printOut)



@click.command()
@click.argument('board', default=os.path.join(os.path.dirname(__file__), 'BoardToSolve.txt'))
def main(board):

	parseTextFile(board)
	print("\nSolving board:\n")
	printBoard(board)
	sys.stdout.flush()
	start_time = time.time()
	solved_board = deepcopy(board)

	y = 0
	while 0 <= y <= 8:
		x = 0
		while 0 <= x <= 8:	
			if board[y][x] != 0:
				x += 1
				continue
			current_num = copy(solved_board[y][x])
			while current_num <= 9:
				current_num += 1
				if isValidInPosition(x, y, current_num, solved_board):
					solved_board[y][x] = current_num
					break			
			if current_num >= 10:
				solved_board[y][x] = 0
				prev_position = findPrevEmptyPosition(x,y)
				x = prev_position[0]
				y = prev_position[1]
			else:
				x += 1
		y = y+1

	end_time = time.time()
	print("Solved it!\n")
	printBoard(solved_board)
	sys.stdout.flush()
	print("Time to solve: " + str(end_time-start_time) + " seconds")


if __name__=="__main__":
	main()

