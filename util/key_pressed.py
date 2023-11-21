from uib_inf100_graphics.event_app import *
import util.help_funcs as hf

def kp_active(app, event):
    if event.key == 'Up' and app.direction != 'south':
        app.direction = 'north'
    if event.key == 'Down' and app.direction != 'north':
        app.direction = 'south'
    if event.key == 'Right' and app.direction != 'west':
        app.direction = 'east'
    if event.key == 'Left' and app.direction != 'east':
        app.direction = 'west'

def kp_menu(app, event):
    app.board = hf.create_board(14, 18)
    app.snake_size = 3
    app.head_pos = (0, 2)
    app.direction = 'east'

    if event.key == 'm':
        if app.gamemode == 'arcade':
            app.gamemode = 'lvl'

            app.arc_font = 'Arial 20'
            app.lvl_font = 'Arial 25 bold'
            app.arc_color = 'white'
            app.lvl_color = 'green'

        else:
            app.gamemode = 'arcade'

            app.arc_font = 'Arial 25 bold'
            app.lvl_font = 'Arial 20'
            app.arc_color = 'green'
            app.lvl_color = 'white'

    if event.key == 'c':
        app.snake_color = hf.increment(app)

    if event.key == 'Space':
        if app.gamemode == 'lvl':
            app.state = 'lvl_info'
        if app.gamemode == 'arcade':
            app.state = 'active'
        