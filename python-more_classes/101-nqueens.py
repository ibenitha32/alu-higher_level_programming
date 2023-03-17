#!/usr/bin/python3

"""
This module contains a function to solve the N-queens problem.
"""

def check_two_queens(position1, position2):
    """
    This function checks if two queens placed at position1 and position2 are
    attacking each other.
    """
    if position1[0] == position2[0] or position1[1] == position2[1]:
        return True
    if abs(position1[0] - position2[0]) == abs(position1[1] - position2[1]):
        return True
    return False

def n_queens(n):
    """
    This function solves the N-queens problem.
    """
    if not isinstance(n, int):
        return None
    if n < 4:
        return None

    possibilty = [[i, j] for i in range(n) for j in range(n) if i < j]

    if not possibilty:
        return None

    i = 0
    count = 0

    while i < len(possibilty) - 1:
        j = i + 1
        while j < len(possibilty):
            if not check_two_queens(possibilty[i], possibilty[j]):
                count += 1
            j += 1
        i += 1

    return count

print(n_queens(2))
