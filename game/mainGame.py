from src import universalVariables as UV
from src import universalFuncs as UFS
from src import spritesModule as SM
import pygame

# Init PyGame.
pygame.init()

# Function to Init My Game (x).
def initGame():

    # My Screen.
    UFS.initScreen()

    # My Loop.
    while UV.run:
        UFS.initLoop() # The Function to Init Main Loop.

        # Fill the Screen whit White Color.
        UV.screen.fill(UV.WHITE)

        # Function to Draw the Pointer Image .
        UFS.drawPointerGame()

        # Update the Code of the Game Constantly.
        pygame.display.update()
