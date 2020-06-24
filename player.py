'''
Created on Jun 23, 2020

@author: Neil
'''
import pygame
import config

class Player:
    def __init__(self, xPos, yPos):
        print("Player created")
        self.position = [xPos, yPos]
        self.image = pygame.image.load("sprites/Tomb Guy Idle.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        scl = config.SCALE
        self.rect = pygame.Rect(self.position[0] * scl, self.position[1] * scl,
                                                scl, scl)
        
    def update(self):
        print("Player updated")
        
    def update_position(self, newPos):
        self.position[0] = newPos[0]
        self.position[1] = newPos[1]
        scl = config.SCALE
        self.rect = pygame.Rect(self.position[0] * scl, self.position[1] * scl,
                                                scl, scl)
    
    def render(self, screen, camera):
        self.rect = pygame.Rect(self.position[0] * config.SCALE - (camera[0] * config.SCALE), self.position[1] * config.SCALE - (camera[1] * config.SCALE), config.SCALE, config.SCALE)
        screen.blit(self.image, self.rect)