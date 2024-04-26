import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bomb_locations = random.sample(range(self.dim_size**2), self.num_bombs)
        for loc in bomb_locations:
            row = loc // self.dim_size
            col = loc % self.dim_size
            board[row][col] = '*'
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] != '*':
                    self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = sum(
            1
            for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1)
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1)
            if self.board[r][c] == '*'
        )
        return num_neighboring_bombs

    def dig(self, row, col):
        self.dug.add((row, col))
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) not in self.dug:
                    self.dig(r, c)
        return True

    def __str__(self):
        visible_board = [[' ' if (r, c) not in self.dug else str(self.board[r][c]) for c in range(self.dim_size)] for r in range(self.dim_size)]
        str_len = max(len(str(cell)) for row in visible_board for cell in row)
        string_rep = '  ' + '  '.join(str(col) for col in range(self.dim_size)) + '  \n'
        for i, row in enumerate(visible_board):
            string_rep += f'{i} | ' + ' | '.join(str(cell).center(str_len) for cell in row) + ' |\n'
        return string_rep + '-' * (self.dim_size * (str_len + 3) + 4)

def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue
        safe = board.dig(row, col)
        if not safe:
            break
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("GAME OVER!!! BETTER LUCK NEXT TIME :(")
        board.dug = set((r, c) for r in range(board.dim_size) for c in range(board.dim_size))
        print(board)

if __name__ == '__main__':
    play()
