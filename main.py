from uib_inf100_graphics.event_app import run_app
from util.help_funcs import *
from util.key_pressed import *
import csv
from util.move_snake import *

DB_PATH = 'db/db.csv'

def app_started(app):
    app.direction = 'east'
    app.debug_mode = False
    app.board = create_board(14, 18)
    app.snake_size = 3
    app.head_pos = (0, 2)
    app.state = 'menu'
    app.gamemode = 'lvl'
    app.level = 1
    app.timer_delay = 100
    app.snake_color = 'blue'
    app.highscore = 0
    app.hearts = 5
    with open(DB_PATH, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            app.highscore = int(row[0])

    app.lvl_font = 'Arial 25 bold'
    app.arc_font = 'Arial 20'
    app.lvl_color = 'green'
    app.arc_color = 'white'

def timer_fired(app):
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    if app.debug_mode == False and app.state == 'active' and app.gamemode == 'arcade':
        move_snake_arcade(app)
    if app.debug_mode == False and app.state == 'active' and app.gamemode == 'lvl' and app.level == 1:
        move_snake_lvl1(app)
    if app.debug_mode == False and app.state == 'active' and app.gamemode == 'lvl' and app.level == 2:
        move_snake_lvl2(app)
    if app.debug_mode == False and app.state == 'active' and app.gamemode == 'lvl' and app.level == 3:
        move_snake_lvl3(app)
    
    


def key_pressed(app, event):
    if event.key == 'd':
        app.debug_mode = not app.debug_mode
    
    if app.state == 'active':
        kp_active(app, event)

    elif app.state == 'menu':
        kp_menu(app, event)
    
    elif app.state == 'gameover':
        if event.key == 'Space':
            app_started(app)
    
    elif app.state == 'lvl_info':
        if event.key == 'Space':
            app.state = 'active'
    
    elif app.state == 'lvl_gameover':
        if event.key == 'Space':
            app_started(app)
    
    elif app.state == 'lvl_victory':
        if event.key == 'Space':
            app_started(app)

def redraw_all(app, canvas):
    # Debug mode
    if app.debug_mode == True:
        draw_debug(app, canvas)

    # State
    if app.state == 'menu':
        draw_menu(app, canvas)
    if app.state == 'gameover':
        draw_gameover(app, canvas)
    if app.state == 'lvl_gameover':
        draw_gameover_lvl(app, canvas)
    if app.state == 'lvl_info':
        draw_lvl_info(app, canvas)
    if app.state == 'lvl_victory':
        draw_lvl_victory(app, canvas)
    if app.state == 'active':
        
        # Mode
        if app.gamemode == 'arcade':
            draw_board(canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.debug_mode, app)
        if app.gamemode == 'lvl':
            if app.level == 1:
                draw_board(canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.debug_mode, app)
            if app.level == 2:
                draw_board(canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.debug_mode, app)
            if app.level == 3:
                draw_board(canvas, 25, 25, app.width - 25, app.height - 25, app.board, app.debug_mode, app)



run_app(width=500, height=400, title="Snake")