from src import spritesModule as SP
import pygame

# Init Pygame
pygame.init()

# Screen Universal Variables
SIZESCREEN = (600, 600) # Size of the Screen 
WIDTHSCREEN, HEIGHTSCREEN = SIZESCREEN # Distribute the Screen size to Width and Height of the Screen
screenName = "Coquillage Project" # That´s the Name who the Screen Will Have
screen = pygame.display.set_mode(SIZESCREEN) # Here I Only Init my Screen Variable
pygame.display.set_caption(screenName) # Here i Put the Name Previously Init

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Detect if the Player Close the Screen
run = True
