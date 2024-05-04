from classGame import universalVariables as UV
import pygame
import sys

# Init Pygame
pygame.init()

# Function to Init the Screen
def initScreen():
    UV.screen

# Function to Init the Main Loop
def initLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Function to Draw all Sprites
