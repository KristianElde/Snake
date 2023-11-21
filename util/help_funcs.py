import random

DB_PATH = './db/db.csv'


def create_board(rows, cols):
    board = []
    for _ in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
            if j == cols - 1:
                board.append(row)
    board[0][0] = 1
    board[0][1] = 2
    board[0][2] = 3
    add_apple_at_random_location(board)
    
    return board

def create_board_lvl2():
    board = [[6,7,0,-2,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0],
             [5,8,0,-2,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0],
             [4,9,0,-2,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0],
             [3,10,0,-2,0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0],
             [2,11,0,-2,0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0],
             [1,12,0,-2,0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0],
             [0,13,0,-2,0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0],
             [0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0],
             [0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0],
             [0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0],
             [0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0,-2,0,0,0],
             [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,-2,0,0,0],
             [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,-2,0,-1,0],
             [0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,-2,0,0,0],]
    return board


def new_head_pos(pos, dir):
    row, col = pos
    if dir == 'north':
        row -= 1
    if dir == 'south':
        row += 1
    if dir == 'west':
        col -= 1
    if dir == 'east':
        col += 1
    
    return (row, col)

def add_apple_at_random_location(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    while True:
        row = random.choice(range(rows))
        col = random.choice(range(cols))
        if grid[row][col] == 0:
            grid[row][col] = -1
            break



def add_bomb_at_random_location(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    while True:
        row = random.choice(range(rows))
        col = random.choice(range(cols))
        if grid[row][col] == 0:
            grid[row][col] = -2
            break

def subtract_one_from_all_positives(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 0:
                grid[i][j] -= 1

def update_highscore(highscore):
    with open(DB_PATH, 'w') as file:
        file.write(f'{highscore}')

def is_legal_move(pos, board, highscore):
    row, col = pos
    rows = len(board)
    cols = len(board[0])
    
    if row not in range(rows):
        update_highscore(highscore)
        return False
    if col not in range(cols):
        update_highscore(highscore)
        return False
    if board[row][col] > 0:
        update_highscore(highscore)
        return False
    if board[row][col] == -2:
        update_highscore(highscore)
        return False
    
    return True

def increment(app):
    color_modes = ['blue', 'green', 'red']
    index = color_modes.index(app.snake_color)
    color = color_modes[(index + 1 + len(color_modes)) % len(color_modes)]

    return color