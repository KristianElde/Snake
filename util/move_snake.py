from uib_inf100_graphics.event_app import run_app
from util.help_funcs import *
from util.snake_view import *
from util.key_pressed import *

def move_snake_arcade(app):
    app.head_pos = new_head_pos(app.head_pos, app.direction)
    row, col = app.head_pos
    highscore = app.highscore

    if is_legal_move(app.head_pos, app.board, highscore) == False:
        app.state = 'gameover'
        return

    if app.board[row][col] == -1:
        app.snake_size += 1
        add_apple_at_random_location(app.board)
        if app.snake_size % 2 == 0:
            add_bomb_at_random_location(app.board)
    else:
        subtract_one_from_all_positives(app.board)
    
    if (app.snake_size - 3) > app.highscore:
        app.highscore = app.snake_size - 3
    
    app.board[row][col] = app.snake_size

def move_snake_lvl1(app):
    app.head_pos = new_head_pos(app.head_pos, app.direction)
    row, col = app.head_pos
    highscore = app.highscore

    if is_legal_move(app.head_pos, app.board, highscore) == False:
        app.hearts -= 1
        if app.hearts == 0:
            app.state = 'lvl_gameover'
        else:
            app.board = hf.create_board(14, 18)
            app.snake_size = 3
            app.head_pos = (0, 2)
            app.direction = 'east'
        return

    if app.board[row][col] == -1:
        app.snake_size += 1
        add_apple_at_random_location(app.board)
        if app.snake_size % 2 == 0:
            add_bomb_at_random_location(app.board)
    else:
        subtract_one_from_all_positives(app.board)
# ENDRE TIL 13
    if app.snake_size == 13:
        app.level += 1
        app.state = 'lvl_info'
        app.board = hf.create_board_lvl2()
        app.snake_size = 13
        app.head_pos = (6, 1)
        app.direction = 'south'

    
    app.board[row][col] = app.snake_size

def move_snake_lvl2(app):
    app.head_pos = new_head_pos(app.head_pos, app.direction)
    row, col = app.head_pos
    highscore = app.highscore

    if is_legal_move(app.head_pos, app.board, highscore) == False:
        app.hearts -= 1
        if app.hearts == 0:
            app.state = 'lvl_gameover'
        else:
            app.board = hf.create_board_lvl2()
            app.snake_size = 13
            app.head_pos = (6, 1)
            app.direction = 'south'
        return

    if app.board[row][col] == -1:
        app.snake_size += 1
        app.board[1][1] = -1
    else:
        subtract_one_from_all_positives(app.board)
    if app.snake_size == 15:
        app.level += 1
        app.state = 'lvl_info'
        app.board = create_board(7, 9)
        app.snake_size = 3
        app.head_pos = (0, 2)
        app.direction = 'east'
        app.time_delay = 40

    
    app.board[row][col] = app.snake_size

def move_snake_lvl3(app):
    app.head_pos = new_head_pos(app.head_pos, app.direction)
    row, col = app.head_pos
    highscore = app.highscore

    if is_legal_move(app.head_pos, app.board, highscore) == False:
        app.hearts -= 1
        if app.hearts == 0:
            app.state = 'lvl_gameover'
        else:
            app.board = create_board(7, 9)
            app.snake_size = 3
            app.head_pos = (0, 2)
            app.direction = 'east'
            app.time_delay = 40
        return

    if app.board[row][col] == -1:
        app.snake_size += 1
        add_apple_at_random_location(app.board)
        if app.snake_size % 2 == 0:
            add_bomb_at_random_location(app.board)
    else:
        subtract_one_from_all_positives(app.board)
    if app.snake_size == 8:
        app.state = 'lvl_victory'

    
    app.board[row][col] = app.snake_size