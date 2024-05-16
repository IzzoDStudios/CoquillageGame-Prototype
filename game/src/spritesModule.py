from src import universalVariables as UV
import pygame

# Init Pygame
pygame.init()

#------------------------------------------Image Zone-----------------------------------------------------------------------------------#
pointerImg = pygame.image.load("img/elegantPointer.png")

#------------------------------------------Classes Zone-----------------------------------------------------------------------------------#
# Pointer Sprite Class
class pointer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pointerImg # Sprite Image
        self.image = pygame.transform.scale(self.image,(200, 200)) # Change the Image Size (Width, Height)
        self.rect = self.image.get_rect() # Add a Collider to the Sprite

#------------------------------------------groups Zone-----------------------------------------------------------------------------------#
allSpritesGroup = pygame.sprite.Group()

#------------------------------------------Variables Zone-----------------------------------------------------------------------------------#
mypointer = pointer()
mypointer.add(allSpritesGroup)
