import pygame
import random
from Class_Snake import *
screenSize = 500
def main():
    #Initialize game
    snake=Snake()
    food=Food()
    tempdirection="Left"
    eat=False
    points = 0
    pygame.init()
    screen = pygame.display.set_mode((screenSize,screenSize))
    running = True
    while running:
        pygame.time.delay(80)
        pygame.display.set_caption("Snake points = " + str(points))
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            tempdirection="Down"
        if key[pygame.K_UP]:
            tempdirection="Up"
        if key[pygame.K_RIGHT]:
            tempdirection="Right"
        if key[pygame.K_LEFT]:
            tempdirection="Left"
        #check if is a valid new direction
        snake.newdirection(tempdirection)
        #check if I'm in the screen
        running = snake.valid()
        #a bool if I am in the position of the food
        eat=snake.move(food)
        #appear a new food 
        if eat is True:
            points = len(snake.body)*23 + points
            while food.pos in snake.body:
                food.pos=((random.randint(1,49)*10),(random.randint(1,49)*10))
        screen.fill((0,0,0))
        for pixel in snake.body:
            pygame.draw.rect(screen,(146, 168, 209),(pixel[0],pixel[1],snake.size,snake.size))
        pygame.draw.rect(screen,(247, 202, 201),(food.pos[0],food.pos[1],food.size,food.size))
        pygame.display.update()
        clock.tick(60)

main()