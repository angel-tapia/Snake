import pygame
def keyReceived(key, direction):
    if key[pygame.K_DOWN]:
        direction = "Down"
    if key[pygame.K_UP]:
        direction = "Up"
    if key[pygame.K_RIGHT]:
        direction = "Right"
    if key[pygame.K_LEFT]:
        direction = "Left"
    return direction

def isPause(key, pause):
    if key[pygame.K_p]:
        pause = not pause
    return pause
        
