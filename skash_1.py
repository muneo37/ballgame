#モジュールのインポート
from tkinter import *
import random
import winsound
#ウィンドウの作成
win = Tk()
cv = Canvas(win, width=640,  height = 480 )
cv.pack()
def init_game():
    global is_gameover, ball_ichi_x, ball_ichi_y
    global ball_idou_x, ball_idou_y, ball_size
    global racket_ichi_x, racket_size, point, speed 
    is_gameover = False
    ball_ichi_x = 0
    ball_ichi_y = 250
    ball_idou_x = 15
    ball_idou_y = -15
    ball_size = 10
    racket_ichi_x = 0
    racket_size = 100
    point = 0
    speed = 50
    win.title("スカッシュゲーム：スタート!！")
def draw_screen():
    cv.delete('all')
    cv.create_rectangle(0, 0, 640, 480, fill="white" , width=0)
def draw_ball():
    cv.create_oval(ball_ichi_x - ball_size, ball_ichi_y - ball_size,  ball_ichi_x + ball_size, ball_ichi_y + ball_size, fill="red")
def draw_racket():
    cv.create_rectangle(racket_ichi_x, 470,racket_ichi_x + racket_size, 480, fill="red")
def move_ball():
    global is_gameover, point, ball_ichi_x, ball_ichi_y, ball_idou_x, ball_idou_y
    if is_gameover: return
    if ball_ichi_x + ball_idou_x < 0 or ball_ichi_x + ball_idou_x > 640:
        ball_idou_x *= -1
    if ball_ichi_y + ball_idou_y < 0:
        ball_idou_y *= -1
    if ball_ichi_y + ball_idou_y > 470 and (racket_ichi_x <= (ball_ichi_x + ball_idou_x) <= (racket_ichi_x + racket_size)):
        ball_idou_y *= -1
    if random.randint(0, 1) == 0:
        ball_idou_x *= -1
    point += 10
    win.title("得点=" + str(point))
    if ball_ichi_y + ball_idou_y >=480:
        is_gameover = True
    win.title("特点=" + str(point)) 
    if ball_ichi_y + ball_idou_y >=480:
        is_gameover = True
    win.title("得点=" + str(point))
    if 0 <= ball_ichi_x + ball_idou_x <= 640:
        ball_ichi_x = ball_ichi_x + ball_idou_x
    if 0 <= ball_ichi_y + ball_idou_y <= 480:
        ball_ichi_y = ball_ichi_y + ball_idou_y
def motion(event):
    global racket_ichi_x
    racket_ichi_x = event.x
def click(event):
    if event.num == 1:
        init_game()
win.bind('<Motion>', motion)
win.bind('<Button>', click)
def game_loop():
    draw_screen()
    draw_ball()
    draw_racket()
    move_ball()
    win.after(speed, game_loop)
init_game()
game_loop()
win.mainloop()