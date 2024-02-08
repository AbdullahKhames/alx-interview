#!/usr/bin/python3
"""
module to solve NQueens problem
"""

from sys import argv


def isQueen(cell: list) -> bool:
    """checks if the cell is nqueen and return true
    else false

    Args:
        cell (list): the cell to check

    Returns:
        bool: true if nqueens else false
    """
    row_number = len(cell) - 1
    diff = 0
    for idx in range(0, row_number):
        diff = cell[idx] - cell[row_number]
        if diff < 0:
            diff *= -1
        if diff == 0 or diff == row_number - idx:
            return False
    return True


def solve(dim: int, row: int, cell: list, output: list):
    """recursively solve NQueens problem

    Args:
        dim (int): dimensions
        row (int): row
        cell (list): cell
        output (list): output
    """
    if row == dim:
        print(output)
    else:
        for col in range(0, dim):
            cell.append(col)
            output.append([row, col])
            if (isQueen(cell)):
                solve(dim, row + 1, cell, output)
            cell.pop()
            output.pop()


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    N = int(argv[1])
except BaseException:
    print('N must be a number')
    exit(1)
if N < 4:
    print('N must be at least 4')
    exit(1)
else:
    output = []
    cell = 0
    solve(int(N), cell, [], output)
