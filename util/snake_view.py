import util.help_funcs as hf

def board_color(val):
    if val == 0:
        return 'black'
    elif val == -1:
        return 'green'
    elif val == -2:
        return 'white'
    elif val > 0:
        return 'black'
    
def snake_color(val, app):
    if app.snake_color == 'blue':
        return 'blue'
    if app.snake_color == 'red':
        return 'red'
    if app.snake_color == 'green':
        return 'green'

def draw_board(canvas, x1, y1, x2, y2, board, debug_mode, app):
    columns = len(board[0])
    rows = len(board)

    board_width = (max(x1,x2)-min(x1,x2))
    board_heigth = (max(y1,y2)-min(y1,y2))

    sqr_width = board_width / columns
    sqr_heigth = board_heigth / rows


    
    for i in range(rows):
        sqr_y1 = y1 + sqr_heigth * i
        for j in range(columns):
            sqr_x1 = x1 + sqr_width * j
            canvas.create_rectangle(
                sqr_x1, sqr_y1,
                sqr_x1 + sqr_width, sqr_y1 + sqr_heigth, 
                fill=board_color(board[i][j]),
                outline='black'
            )
            if board[i][j] > 0:
                color = snake_color(board[i][j], app)
                canvas.create_oval(sqr_x1, sqr_y1,
                sqr_x1 + sqr_width, sqr_y1 + sqr_heigth, 
                fill=color
                )
            if debug_mode == True:
                canvas.create_text(
                    sqr_x1 + sqr_width / 2,
                    sqr_y1 + sqr_heigth / 2,
                    text=board[i][j],
                    font='Arial 10',
                    fill='lightgrey'
                )
    if app.gamemode == 'lvl':
        _x1 = 30
        y1=30
        for i in range(5):
            x1 = _x1 + i * 22
            canvas.create_oval(x1, y1, x1 + 20, y1 + 20, fill = 'white')
        _x1 = 32
        y1 = 32
        for i in range(app.hearts):
            x1 = _x1 + i * 22
            canvas.create_oval(x1, y1, x1 + 16, y1 + 16, fill = 'red')

    if app.gamemode == 'arcade':
        canvas.create_text(
            app.width / 2,
            10,
            text=f'Highscore: {app.highscore}',
            font='Arial 15',
            fill = 'black'
        )
    if app.level != 2:
        canvas.create_text(
                app.width / 2,
                app.height / 2,
                text=app.snake_size - 3,
                font='Arial 50',
                fill = 'white'
            )

def draw_menu(app,canvas):
    canvas.create_rectangle(25,25,app.width-25,app.height-25,fill='black')

    canvas.create_text(
            app.width / 2,
            app.height * (1/6),
            text='Main menu',
            font='Arial 20',
            fill='white'
        )


    canvas.create_text(
            app.width * (1/3),
            app.height / 2,
            text='Arcade',
            font=app.arc_font,
            fill=app.arc_color
        )
    
    _x1 = 160
    y1 = 130
    for i in range(6):
        x1 = _x1 + 30 * i
        color = snake_color(i, app)
        canvas.create_oval(x1,y1,x1 + 30, y1 + 30, fill=color)
    
    canvas.create_text(
            app.width * (2/3),
            app.height / 2,
            text='Levels',
            font=app.lvl_font,
            fill=app.lvl_color
        )

    canvas.create_text(
            app.width / 2,
            app.height * (3/4),
            text="Press 'm' to switch gamemode\nPress 'c' to change color of your snake\nPress 'Space' to start a new game",
            font='Arial 10',
            fill='white'
        )
    
def draw_gameover(app, canvas):
    canvas.create_text(
            app.width / 2,
            app.height / 2,
            text='Game Over',
            font='Arial 30',
        )

    canvas.create_text(
            app.width / 2,
            app.height - (app.height / 3),
            text=f'Your score: {app.snake_size - 3}',
            font='Arial 20',
        )

    canvas.create_text(
            app.width / 2,
            app.height - (app.height / 5),
            text='Press space to proceed to menu',
            font='Arial 15',
        )
    
def draw_gameover_lvl(app, canvas):
    canvas.create_text(
            app.width / 2,
            app.height / 2,
            text='Game Over',
            font='Arial 30',
        )

    canvas.create_text(
            app.width / 2,
            app.height - (app.height / 3),
            text=f'You reached level {app.level}',
            font='Arial 20',
        )

    canvas.create_text(
            app.width / 2,
            app.height - (app.height / 5),
            text='Press space to proceed to menu',
            font='Arial 15',
        )
    

def draw_arcade(app, canvas):
    hf.draw_board(canvas, 
                25, 25, app.width - 25, app.height - 25,
                app.board,
                app.debug_mode,
                app)
    
def draw_debug(app, canvas):
    canvas.create_text(
        app.width / 2, 10,
        text=f"app.head_pos={app.head_pos} app.direction='{app.direction}' app.state={app.state} app.gamemode={app.gamemode}",
        font = 'Arial 10',
    )

def draw_level_1(app, canvas):
    draw_board(canvas,
        25, 25, app.width - 25, app.height - 25,
        app.board,
        app.debug_mode,
        app)
    
    
def draw_lvl_info(app, canvas):
    canvas.create_rectangle(25,25,app.width-25,app.height-25,fill='black')

    canvas.create_text(
            app.width / 2,
            app.height * (1/6),
            text=f'Level {app.level}',
            font='Arial 40',
            fill='white'
        )

    if app.level == 1:
        canvas.create_text(
            app.width / 2,
            app.height / 2,
            text='Eat 10 apples to complete this level',
            font='Arial 18',
            fill='white'
        )

    if app.level == 2:
        canvas.create_text(
            app.width / 2,
            app.height / 2,
            text='Eat 2 apples, but avoid the walls!',
            font='Arial 18',
            fill='white'
        )

    if app.level == 3:
        canvas.create_text(
            app.width / 2,
            app.height / 2,
            text='Can you handle faster pace,\n and a smaller board?\nEat 5 apples to complete this level',
            font='Arial 18',
            fill='white'
        )
    
    canvas.create_text(
            app.width / 2,
            app.height * (3/4),
            text="Press 'Space' to start level",
            font='Arial 10',
            fill='white'
        )
    
def draw_lvl_victory(app, canvas):
    canvas.create_rectangle(25,25,app.width-25,app.height-25,fill='black')

    canvas.create_text(
            app.width / 2,
            app.height / 2,
            text='VICTORY!',
            font='Arial 40',
            fill='white'
        )
    
    canvas.create_text(
            app.width / 2,
            app.height - (app.height / 5),
            text='Press space to proceed to menu',
            font='Arial 15',
            fill ='white',
        )