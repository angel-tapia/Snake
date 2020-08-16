import pygame
import random
screenSize = 500
directions = ["Left","Up","Right","Down"]
class Snake:
    def __init__ (self):
        self.size = 10
        self.speed = 10
        #body[i][0]=x and body[i][1]=y
        self.body = [(screenSize/2,screenSize/2)]
        self.direction = "Left"

    def move(self):
        mov = [(-self.speed,0),(0,-self.speed),(self.speed,0),(0,self.speed) ]
        (x,y)=self.body[0]
        idx = directions.index(self.direction)
        (dx,dy)=mov[idx]
        newHead = (x+dx,y+dy)
        self.body.insert(0,newHead)

    def valid(self):
        (x,y) = self.body[0]
        if x < 0 or x > screenSize-self.size or y < 0 or y > screenSize-self.size:
            return False
        head = self.body[0]
        if self.body.count(head) > 1:
            return False
        return True

    def setDirection(self, direction):
        if len(self.body) is 1:
            self.direction = direction
            return
        indexDir = directions.index(self.direction)
        indexNewDir = directions.index(direction)
        if (indexDir+2)%4 is not indexNewDir:
            self.direction = direction

    def pop(self):
        self.body.pop()

class Food:
    def __init__ (self):
        self.size = 10
        self.pos = ((random.randint(1,49)*10),(random.randint(1,49)*10))

    def appearFood(self, snake):
         #while the new food is in the body of the snake appear a new food
        while self.pos in snake.body:
            self.pos = ((random.randint(1,49)*10),(random.randint(1,49)*10))
