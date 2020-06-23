'''
Created on Jun 23, 2020

@author: Neil
'''
from player import Player
from game_state import GameState
import config
import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        
    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        self.game_state = GameState.RUNNING
        print("set up")
    
    def update(self):
        #clear screen first
        self.screen.fill(config.BLACK)
        print("update")
        #handle all events related to the object
        self.handle_events()
        
        #every object in objects should have a render function
        for object in self.objects:
            object.render(self.screen)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN: #all keyboard commands
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_w: #up
                    self.player.update_position(0, -1)
                elif event.key == pygame.K_a: #left
                    self.player.update_position(-1, 0)
                elif event.key == pygame.K_s: #down
                    self.player.update_position(0, 1)
                elif event.key == pygame.K_d: #right
                    self.player.update_position(1, 0)