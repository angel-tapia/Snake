import pygame
import random
from Constants import *
from Class_Snake import *
from Interactions_Py import *

class Game:

    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.eat = False
        self.newDirection = "Left"
        self.points = 0
        pygame.init()
        self.screen = pygame.display.set_mode((screenSize,screenSize))
        self.running = True
        self.pause = False

    def simulate(self):
        pygame.time.delay(80)
        #Check if is finished 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

        #receive key
        self.key = pygame.key.get_pressed()

        #Check if is paused the game
        self.pause = isPause(self.key, self.pause)
        if self.pause is True:
            self.key = pygame.K_u
            return

        #check if is a valid new direction
        self.newDirection = parsingKey(self.key, self.newDirection)
        self.snake.setDirection(self.newDirection)

        #check if I'm in the screen
        if self.snake.valid() is False:
            self.running = False
            return

        #move the snake
        self.snake.move()

        #appear a new food if I'm in the position of the food
        if self.food.pos in self.snake.body:
            self.points = (len(self.snake.body)-1)*random.randint(1,13) + self.points
            self.food.appearFood(self.snake)
        else :
            self.snake.pop()

    def draw(self):
        #Display points obtained actually
        pygame.display.set_caption("Snake points = " + str(self.points))
        
        #Draw
        self.screen.fill((0,0,0))
        for pixel in self.snake.body:
            pygame.draw.rect(self.screen,(146, 168, 209),(pixel[0],pixel[1],pixelSize,pixelSize))
        pygame.draw.rect(self.screen,(247, 202, 201),(self.food.pos[0],self.food.pos[1],pixelSize,pixelSize))
        pygame.display.update()

