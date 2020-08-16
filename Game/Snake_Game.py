import pygame
import random
from Class_Snake import *
from Interactions_Py import *
screenSize = 500
def main():
    #Initialize game
    snake=Snake()
    food=Food()
    eat=False
    newDirection="Left"
    points = 0
    pygame.init()
    screen = pygame.display.set_mode((screenSize,screenSize))
    running = True
    pause = False
    while running:
        pygame.time.delay(80)
        #Display points obtained
        pygame.display.set_caption("Snake points = " + str(points))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()
        #Check if is paused the game
        pause=isPause(key,pause)
        if pause is True:
            continue
        newDirection=keyReceived(key,newDirection)
        #check if is a valid new direction
        snake.newdirection(newDirection)
        #check if I'm in the screen
        running = snake.valid()
        #a bool if I am in the position of the food
        eat=snake.move(food)
        #appear a new food 
        if eat is True:
            points = (len(snake.body)-1)*23 + points
            food.appearFood(snake)
        #Draw
        screen.fill((0,0,0))
        for pixel in snake.body:
            pygame.draw.rect(screen,(146, 168, 209),(pixel[0],pixel[1],snake.size,snake.size))
        pygame.draw.rect(screen,(247, 202, 201),(food.pos[0],food.pos[1],food.size,food.size))
        pygame.display.update()

main()
