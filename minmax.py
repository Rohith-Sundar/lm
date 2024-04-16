import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    # Check if the board is full
    return all(cell != ' ' for row in board for cell in row)

def get_available_moves(board):
    # Return a list of empty cells
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'X'):
        return -1
    elif is_winner(board, 'O'):
        return 1
    elif is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 'O'
        eval = minimax(board, 0, False)
        board[move[0]][move[1]] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        player_move = tuple(map(int, input("Enter your move (row and column): ").split()))

        if board[player_move[0]][player_move[1]] != ' ':
            print("Cell already taken. Try again.")
            continue

        board[player_move[0]][player_move[1]] = 'X'

        if is_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        print("Computer's move:")
        computer_move = find_best_move(board)
        board[computer_move[0]][computer_move[1]] = 'O'

        if is_winner(board, 'O'):
            print_board(board)
            print("Computer wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
