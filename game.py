'''
Created on Jun 23, 2020

@author: Neil
'''
from player import Player
from game_state import GameState
import config
import pygame
import math

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.map = []
        self.game_state = GameState.NONE
        self.camera = [0, 0]
        
    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        self.game_state = GameState.RUNNING
        self.load_map("01")
    
    def update(self):
        #clear screen first
        self.screen.fill(config.GREEN)
        #print("update")
        #handle all events related to the object
        self.handle_events()
        
        self.render_map(self.screen)
        
        #every object in objects should have a render function
        for object in self.objects:
            object.render(self.screen, self.camera)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN: #all keyboard commands
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_w: #up
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_a: #left
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_s: #down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_d: #right
                    self.move_unit(self.player, [1, 0])
    
    def load_map(self, file_name):
        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)
    
    def render_map(self, screen):
        self.determine_camera()
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE - (self.camera[0] * config.SCALE), y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos += 1
            y_pos += 1
    
    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]
        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return
        if new_position[1] < 0 or new_position[1] > (len(self.map) - 1):
            return
        if self.map[new_position[1]][new_position[0]] == "W": #collision with wall
            return
        
        unit.update_position(new_position)
    
    def determine_camera(self):
        #determine y pos of cam
        max_y_position = len(self.map) - config.SCREEN_HEIGHT / config.SCALE
        y_position = self.player.position[1] - math.ceil(round(config.SCREEN_HEIGHT / config.SCALE / 2))
        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position
        
        #determine x pos
        max_x_position = len(self.map[0]) - config.SCREEN_WIDTH / config.SCALE
        x_position = self.player.position[0] - math.ceil(round(config.SCREEN_WIDTH / config.SCALE / 2))
        if x_position <= max_x_position and x_position >= 0:
            self.camera[0] = x_position
        elif x_position < 0:
            self.camera[0] = 0
        else:
            self.camera[0] = max_x_position
            

map_tile_image = config.map_tile_image
            
            