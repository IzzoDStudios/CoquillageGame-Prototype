from settings import universalVariables as UV
from settings import universalFuncs as UFS
import pygame
import sys

# init PyGame
pygame.init()

# Function to Init My Game (x)
def initGame():

    # My Screen
    UFS.initScreen()

    # My Loop
    while UV.run:
        UFS.initLoop() # The Function to Init Main Loop

    # Fill the Screen
    UV.screen.fill(UV.WHITE)
    
    # Update the Code of the Game Constantly
    pygame.display.update()
