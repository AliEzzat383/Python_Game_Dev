from turtle import delay
import pygame
from rgb import *
class Blocks:
    randx,randy = random.randint(-10, 10),random.randint(-10, 10)
    
    def __init__(self, x, y, w, h, color,display):
        
        

        self.B_loc = {'X': x, 'Y': y}
        self.B_size = {'width': w, 'height': h}
        self.W = w
        self.H = h
        self.top_left = [y,x]
        self.top_right= [y,x+w]
        self.bottom_left =[y+h,x]
        self.bottom_right =[y+h,x+w]
        self.centerX = x - (self.H/2)
        self.centerY = y - (self.W/2)
        self.X = self.centerX #x
        self.Y = self.centerY #y
        self.color = color
        self.display = display
        self.dx = 0
        self.dy = 0 
        self.lastmove=""
        self.score = 0
        print(self.top_left,self.top_right,self.bottom_left,self.bottom_right)

    def is_under(self,obj):
        self.new_coordinates()
        if(self.top_left[0]>(obj.top_left[0])):                                         # top ball to bottom racket
            return True
        else:
            return False
        

         
    def move_block(self):
        self.X += self.dx
        self.Y += self.dy

    def move_racket(self,last):
        self.lastmove = last
        keys = pygame.key.get_pressed()
        keypressed=False
        if keys[pygame.K_RIGHT] and last !="right":
            self.dx =  10
            self.lastmove  = "right"
            keypressed= True
        elif keys[pygame.K_LEFT] and last !="left":
            self.dx =  -10
            self.lastmove  = "left"
            keypressed= True
        elif self.X <= 0 or (self.X + self.W) >= (500):
            self.dx = 0
            keypressed=False
        self.move_block()
        return keypressed

    def start_move(self):
        self.dx,self.dy = self.randx,self.randy

    def bounce_ball_racket(self,racket):
        self.new_coordinates()
        racket.new_coordinates()
        if self.X <= 0 or self.X >= (480) :
            self.dx = self.dx * -1
        if (self.top_left[0] <= 0) or ((self.bottom_left[0] >= racket.top_left[0]) and ((self.top_right[1] >= racket.top_left[1]) and (self.top_left[1] <= racket.top_right[1]))):
            self.dy = self.dy * -1
            self.score += 1


    def bounce_ball_border(self):
        if self.X <= 0 or self.X >= (480):
            self.dx = self.dx * -1
        if self.Y <= 0 or self.Y >= (480):
            self.dy = self.dy * -1

    def draw_block(self,display):
        pygame.draw.rect(display,self.color,(self.X,self.Y,self.W,self.H))

    def new_coordinates(self):
        self.top_left     = [self.Y , self.X]
        self.top_right    = [self.Y , self.X+self.W]
        self.bottom_left  = [self.Y+self.H , self.X]
        self.bottom_right = [self.Y+self.H , self.X+self.W]




    # def move_gravity(self):
    #     self.X += self.dx
    #     self.Y += self.dy
        