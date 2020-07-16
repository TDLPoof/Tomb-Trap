'''
Created on Jun 23, 2020

@author: Neil
'''
import pygame
import config

class Player:
    def __init__(self, xPos, yPos):
        self.position = [xPos, yPos]
        self.image = pygame.image.load("sprites/Tomb Guy Idle.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        scl = config.SCALE
        self.rect = pygame.Rect(self.position[0] * scl, self.position[1] * scl, scl, scl)

    def change_sprite(self, imageNum):
        if imageNum == 0:
            self.image = pygame.image.load("sprites/Tomb Guy Idle.png")
        if imageNum == 1:
            self.image = pygame.image.load("sprites/Tomb Guy Right.png")
        if imageNum == 2:
            self.image = pygame.image.load("sprites/Tomb Guy Left.png")
        if imageNum == 3:
            self.image = pygame.image.load("sprites/Tomb Guy Back.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))

    def update(self):
        print("Player updated")

    def update_position(self, newPos):
        self.position[0] = newPos[0]
        self.position[1] = newPos[1]
        scl = config.SCALE
        self.rect = pygame.Rect(self.position[0] * scl, self.position[1] * scl, scl, scl)

    def render(self, screen, camera):
        self.rect = pygame.Rect(self.position[0] * config.SCALE - (camera[0] * config.SCALE), self.position[1] * config.SCALE - (camera[1] * config.SCALE), config.SCALE, config.SCALE)
        screen.blit(self.image, self.rect)

    def camo_player(self, tile = "|"):
        # unfortunately, this has to be done
        if tile == "S":
            self.image = pygame.image.load("sprites/Sand.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        if tile == "W":
            self.image = pygame.image.load("sprites/Wall.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        if tile == "D":
            self.image = pygame.image.load("sprites/Door.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        if tile == "E":
            self.image = pygame.image.load("sprites/Exit.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))  
        if tile == "B":
            self.image = pygame.image.load("sprites/Black Tile.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        if tile == "X":
            self.image = pygame.image.load("sprites/White Tile.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))  
        if tile == "C":
            self.image = pygame.image.load("sprites/Cracked Tile.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        if tile == "H":
            self.image = pygame.image.load("sprites/Hole.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        if tile == "J":
            self.image = pygame.image.load("sprites/Jump Tile.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        if tile == "I":
            self.image = pygame.image.load("sprites/Ice.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        if tile == "_":
            self.image = pygame.image.load("sprites/Black.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))  
        if tile == "|":
            self.image = pygame.image.load("sprites/Camo.png")
            self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))

