from src.sprites.spritesVariables import myPointer
from src import universalVariables as UV
from src import universalFuncs as UFS
import pygame
import sys

# Init PyGame
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

        mousepos = pygame.mouse.get_pos()

        myPointer.rect.center = mousepos

        # Update the Code of the Game Constantly
        pygame.display.flip()


initGame()