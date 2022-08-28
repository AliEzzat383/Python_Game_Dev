from pickle import TRUE
import pygame
from blocks import * 
from rgb import *
from background import *
import time

fps = 25

pygame.init()
pygame.display.set_caption('SNAKE')
dis = pygame.display.set_mode((500, 500))
a,b = random_loc(500,500)
snake = []

head = Blocks(30, 30, 25, 25, rand_color(),dis)
snake.append(head)
x=2
while x != 0:
    create_child(snake,dis)
    x-=1

food = Blocks(a,b, 15, 15, rand_color(),dis)

dis.fill(black)

def draw_screen(display):
    display.fill(black)
    pygame.draw.rect(display, food.color, (a,b, food.W, food.H))
    for obj in snake:
        pygame.draw.rect(display,obj.color,(obj.X,obj.Y,obj.W,obj.H))
    pygame.display.update()
dx,dy = 0,0
lastmove = ""
pause = True
eaten = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.Clock().tick(fps)
    draw_screen(dis)
    write_score(dis,eaten)
    dx,dy,lastmove = head.move(dx,dy,lastmove)
    size = len(snake) - 1
    i = 0
    while size > 0:
        # snake[i+1].move_child(snake[i].X,snake[i].Y)
        snake[i+1].move_snake(snake[i])
        size -= 1
        i += 1
    if(head.is_eating(food, a,b)):
        eaten += 1
        # head.draw_snake(dis)
        a,b =random_loc(400,400)
        create_child(snake,dis)
    if head.is_border():
        write_stuff(dis,'YOU LOST', 24, red, 179, 230)
        eaten = 0
        running = False
        