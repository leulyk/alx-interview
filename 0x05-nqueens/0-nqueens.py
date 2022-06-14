#!/usr/bin/python3

"""
    Interview preparation: N-queens
    The N queens puzzle is the challenge of placing N non-attacking queens on
    an N×N chessboard. Write a program that solves the N queens problem.
"""

import sys


def isSafe(board, r, c):
    """ check if two queens threaten each other or not """
    for i in range(r):
        if board[i][c] == 'Q':
            return False

    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    (i, j) = (r, c)
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1

    return True


def generateSolution(board):
    """ generates every possible solution """
    solution = []
    for row_index in range(len(board)):
        for col_index in range(len(board[row_index])):
            if board[row_index][col_index] == 'Q':
                solution.append([row_index, col_index])
    print(solution)


def nQueen(board, r):
    """ evaluates the different combinations recursively """
    if r == len(board):
        generateSolution(board)
        return

    for i in range(len(board)):
        if isSafe(board, r, i):
            board[r][i] = 'Q'
            nQueen(board, r + 1)
            board[r][i] = '–'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        length = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if length < 4:
        print('N must be at least 4')
        sys.exit(1)
    board = [['-' for x in range(length)] for y in range(length)]
    nQueen(board, 0)
