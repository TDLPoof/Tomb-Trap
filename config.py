'''
Created on Jun 23, 2020

@author: Neil
'''
import pygame

BLACK = (0, 0, 0)
GREEN = (0, 160, 0)
WHITE = (255, 255, 255)

SCALE = 32

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

map_tile_image = {
    "S" : pygame.transform.scale(pygame.image.load("sprites/Sand.png"), (SCALE, SCALE)),
    "W": pygame.transform.scale(pygame.image.load("sprites/Wall.png"), (SCALE, SCALE)),
    "B": pygame.transform.scale(pygame.image.load("sprites/Black Tile.png"), (SCALE, SCALE)),
}
