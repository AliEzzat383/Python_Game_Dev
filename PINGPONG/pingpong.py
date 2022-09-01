import pygame
from background import reset, write_score, write_stuff
from blocks import *
from rgb import *

running = True
fps = 30 
# dx,dy = 0,0
lastmove = ""
def draw_screen(display):
    display.fill(black)
    ball.draw_block(display)
    racket.draw_block(display)
    pygame.display.update()

pygame.init()
pygame.display.set_caption('ping pong')
dis = pygame.display.set_mode((500, 500))

ball = Blocks(250,250,20,20,rand_color(),dis)
racket = Blocks(250,490,150,10,rand_color(),dis)
restart = False

ball.start_move()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(fps)
    if(ball.is_under(racket)):
        restart = True
    ball.bounce_ball_racket(racket)

    # ball.bounce_ball_border()
    if restart:
        ball.dx,ball.dy=0,0
        ball.X,ball.Y=ball.centerX,ball.centerY
        if racket.move_racket(racket.lastmove):
            reset(ball)
            write_score(dis,ball.score)
            restart = False
    else:
        ball.move_block()    
        racket.move_racket(racket.lastmove)
    
    draw_screen(dis)
    write_score(dis,ball.score)    
    