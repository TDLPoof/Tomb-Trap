'''
Created on Jun 23, 2020

@author: Neil
'''
import pygame

BLACK = (8, 8, 16)
GREEN = (0, 160, 0)
WHITE = (255, 255, 255)

SCALE = 32

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

map_tile_image = {
    "S": pygame.transform.scale(pygame.image.load("sprites/Sand.png"), (SCALE, SCALE)),
    "W": pygame.transform.scale(pygame.image.load("sprites/Wall.png"), (SCALE, SCALE)),
    "B": pygame.transform.scale(pygame.image.load("sprites/Black Tile.png"), (SCALE, SCALE)),
    "X": pygame.transform.scale(pygame.image.load("sprites/White Tile.png"), (SCALE, SCALE)),
    "D": pygame.transform.scale(pygame.image.load("sprites/Door.png"), (SCALE, SCALE)),
    "I": pygame.transform.scale(pygame.image.load("sprites/Ice.png"), (SCALE, SCALE)),
    "J": pygame.transform.scale(pygame.image.load("sprites/Jump Tile.png"), (SCALE, SCALE)),
    "E": pygame.transform.scale(pygame.image.load("sprites/Exit.png"), (SCALE, SCALE)), 
    "C": pygame.transform.scale(pygame.image.load("sprites/Cracked Tile.png"), (SCALE, SCALE)),
    "H": pygame.transform.scale(pygame.image.load("sprites/Hole.png"), (SCALE, SCALE)),
    "_": pygame.transform.scale(pygame.image.load("sprites/Black.png"), (SCALE, SCALE)),
    "-": pygame.transform.scale(pygame.image.load("sprites/Black.png"), (SCALE, SCALE)),
    "|": pygame.transform.scale(pygame.image.load("sprites/Camo.png"), (SCALE, SCALE)),
    "R": pygame.transform.scale(pygame.image.load("sprites/Red Door.png"), (SCALE, SCALE)),
    "G": pygame.transform.scale(pygame.image.load("sprites/Green Door.png"), (SCALE, SCALE)),
    "F": pygame.transform.scale(pygame.image.load("sprites/Blue Door.png"), (SCALE, SCALE)),
    "0": pygame.transform.scale(pygame.image.load("sprites/Red Switch.png"), (SCALE, SCALE)),
    "1": pygame.transform.scale(pygame.image.load("sprites/Green Switch.png"), (SCALE, SCALE)),
    "2": pygame.transform.scale(pygame.image.load("sprites/Blue Switch.png"), (SCALE, SCALE)),
    "^": pygame.transform.scale(pygame.image.load("sprites/Lobby1.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    "*": pygame.transform.scale(pygame.image.load("sprites/Lobby2.png"), (SCREEN_WIDTH, SCREEN_HEIGHT)),
    "K": pygame.transform.scale(pygame.image.load("sprites/Diamond.png"), (SCALE, SCALE)),
    "!": pygame.transform.scale(pygame.image.load("sprites/Fade U.png"), (SCALE, SCALE)),
    "@": pygame.transform.scale(pygame.image.load("sprites/Fade R.png"), (SCALE, SCALE)),
    "#": pygame.transform.scale(pygame.image.load("sprites/Fade L.png"), (SCALE, SCALE)),
    "$": pygame.transform.scale(pygame.image.load("sprites/Fade D.png"), (SCALE, SCALE)),
    "%": pygame.transform.scale(pygame.image.load("sprites/Fade UR.png"), (SCALE, SCALE)),
    "&": pygame.transform.scale(pygame.image.load("sprites/Fade UL.png"), (SCALE, SCALE)),
    "(": pygame.transform.scale(pygame.image.load("sprites/Fade DR.png"), (SCALE, SCALE)),
    ")": pygame.transform.scale(pygame.image.load("sprites/Fade DL.png"), (SCALE, SCALE)),

}
