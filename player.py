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
    def update(self):
        print("Player updated")
        
    def update_position(self, x_change, y_change):
        self.position[0] += x_change
        self.position[1] += y_change
    
    def render(self, screen):
        scl = config.SCALE
        pygame.draw.rect(screen, config.WHITE, (self.position[0] * scl, self.position[1] * scl,
                                                scl, scl), 4) #controls width of line