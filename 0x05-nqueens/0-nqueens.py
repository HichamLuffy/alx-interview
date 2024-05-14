#!/usr/bin/python3
"""N-Queens Problem"""
import sys


def check_input():
    """"Checks if the correct number of arguments is provided"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def is_safe(board, row, col):
    """"Checks if placing a queen at (row, col) does not lead to conflicts"""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens(N, board, col):
    """Recursive function to place queens on the chessboard"""
    if col == N:
        print_solution(board)
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(N, board, col + 1)
            board[col] = None


def print_solution(board):
    """Formats and prints the board configuration as a list of lists"""
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)


def main():
    """Main function to run the program"""
    N = check_input()  # Validates and retrieves N
    board = [None] * N  # Initializes the board with None
    solve_nqueens(N, board, 0)  # Starts the recursive solving process


if __name__ == "__main__":
    main()
