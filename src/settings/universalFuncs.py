from settings import universalVariables as UV
import pygame
import sys

# Function to Init the Screen
def initScreen():
    screen = pygame.display.set_mode(UV.SIZESCREEN, pygame.FULLSCREEN)

def initLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
