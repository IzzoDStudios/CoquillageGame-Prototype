from src import spritesModule as SM
from src import universalVariables as UV
import pygame
import sys

# Init Pygame.
pygame.init()

# Function to Init the Screen.
def initScreen():
    UV.screen

# Function to Init the Main Loop.
def initLoop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Function to Assign the Amount of Fps.
def assignFps(*, fpsNum):
    UV.FPS.tick(fpsNum) # Assing the Fps.

# Function to Draw the Pointer 
def drawPointerGame():
    # Set and Get Pointer and Mouse Position.
    mousepos = pygame.mouse.get_pos() # Whe Get the Mouse Pointer Position.
    pointerX = mousepos[0] - 96.25 # Position X of the Mouse Pointer - 96.25 (This is to center the image from the pointer to the mouse pointer).
    pointerY = mousepos[1] - 97 # Position Y of the Mouse Pointer - 97 (This is to center the image from the pointer to the mouse pointer).

    pygame.mouse.set_visible(0) # This makes the default cursor invisible.

    # Draw the Pointer in the Screen.
    UV.screen.blit(SM.mypointer.image, (pointerX, pointerY)) #Structure: (Where will the image be drawn?, (Posiion of Drawing)).
