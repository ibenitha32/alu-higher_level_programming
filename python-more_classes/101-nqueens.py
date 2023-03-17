#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def nqueens(board, row, n):
    if row == n:
        print(board)
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            nqueens(board, row + 1, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n
    nqueens(board, 0, n)
