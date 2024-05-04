from settings import universalVariables as UV
import pygame
import sys

# Function to Init the Screen
def initScreen():
    UV.screen

# Function to Init the Main Loop
def initLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
