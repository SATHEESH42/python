import random
import sys

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def drop_bubble(board, col, bubble):
    for row in reversed(board):
        if row[col] == '.':
            row[col] = bubble
            return True
    return False

def check_win(board, bubble):
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == bubble:
                # Check horizontal
                if c + 3 < cols and all(board[r][c+i] == bubble for i in range(4)):
                    return True
                # Check vertical
                if r + 3 < rows and all(board[r+i][c] == bubble for i in range(4)):
                    return True
                # Check diagonal /
                if r + 3 < rows and c + 3 < cols and all(board[r+i][c+i] == bubble for i in range(4)):
                    return True
                # Check diagonal \
                if r - 3 >= 0 and c + 3 < cols and all(board[r-i][c+i] == bubble for i in range(4)):
                    return True
    return False

def main():
    rows, cols = 6, 7
    board = [['.' for _ in range(cols)] for _ in range(rows)]
    bubbles = ['O', 'X']
    turn = 0

    print("Welcome to Bubble Connect Four!")
    print_board(board)

    while True:
        bubble = bubbles[turn % 2]
        print(f"Player {bubble}'s turn.")
        try:
            col = int(input(f"Choose column (0-{cols-1}): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue
        if not (0 <= col < cols):
            print("Column out of range. Try again.")
            continue
        if not drop_bubble(board, col, bubble):
            print("Column full. Try another.")
            continue
        print_board(board)
        if check_win(board, bubble):
            print(f"Player {bubble} wins!")
            break
        if all(board[0][c] != '.' for c in range(cols)):
            print("It's a draw!")
            break
        turn += 1

if __name__ == "__main__":
    main()