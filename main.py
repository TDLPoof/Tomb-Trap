'''
Created on Jun 23, 2020    

Based on tutorial at https://www.youtube.com/watch?v=6oVZ-VBaC2E

@author: Neil
'''
import pygame
import time
import config
from game_state import GameState
from game import Game

def main(width = 2000, height = 2000, frameRate = 60):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Puzzle Game")
    game = Game(screen)
    game.set_up(0)
    
    clock = pygame.time.Clock()
    #main loop
    while game.game_state == GameState.RUNNING:
        clock.tick(frameRate)
        game.update()
        pygame.display.flip()

main(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
