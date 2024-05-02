from settings import universalVariables as UV
from settings import universalFuncs as UFS
import pygame
import sys

# init Python
pygame.init()

def initGame():

    # My Screen
    UFS.initScreen()

    while UV.run:
        UFS.initLoop()
