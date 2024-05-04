from pygame import sprite
import pygame

# Init Pygame
pygame.init()

class pointer(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("spritesImg/pointer.png")
        self.surface 
        self.rect = self.image.get_rect()

