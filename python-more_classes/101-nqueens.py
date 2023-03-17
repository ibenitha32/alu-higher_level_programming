#!/usr/bin/python3
"""
N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
"""

import sys


def is_safe_pos(possibilty, col):
    """Check if it is possible to put the queen"""
    for i in range(col):
        if possibilty[i] == possibilty[col] or abs(possibilty[i] - possibilty[col]) == col - i:
            return False
    return True


def nqueens(possibilty, col, n):
    """Recursive function to place queens on the chess board"""
    count = 0
    if col == n:
        return 1
    for i in range(n):
        possibilty[col] = i
        if is_safe_pos(possibilty, col):
            count += nqueens(possibilty, col + 1, n)
    return count


if __name__ == "__main__":
    # Verify the input
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

    # Initialize an array to hold positions of queens
    possibilty = [0 for i in range(n)]

    # Calculate the number of possible solutions
    count = nqueens(possibilty, 0, n)

    # Print the number of solutions
    print(count)
