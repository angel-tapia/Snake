import pygame
def keyReceived(key,direction):
    if key[pygame.K_DOWN]:
        direction="Down"
    if key[pygame.K_UP]:
        direction="Up"
    if key[pygame.K_RIGHT]:
        direction="Right"
    if key[pygame.K_LEFT]:
        direction="Left"
    return direction

def pause(key):
    if key[pygame.K_p]:
        while key[pygame.K_d]:
            key = pygame.key.get_pressed()
            delay(1000)
        