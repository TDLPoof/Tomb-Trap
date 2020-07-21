

'''
Created on Jun 23, 2020

@authors: Neil and Sasha
'''
from player import Player
from game_state import GameState
import config
import pygame
import math
import time

pygame.mixer.init()

jumpSound = pygame.mixer.Sound("audio/jumpTile.wav")
doorOpen = pygame.mixer.Sound("audio/doorOpen.wav")
colorDoorOpen = pygame.mixer.Sound("audio/colorDoorOpen.wav")
winSound = pygame.mixer.Sound("audio/youWin.wav")
tileSwitch = pygame.mixer.Sound("audio/tileFlip.wav")
tileBreak = pygame.mixer.Sound("audio/tileBreak.wav")
diamondGet = pygame.mixer.Sound("audio/diamondGet.wav")

def hasBlackTiles(map):
        for row in map:
            if row.count("B") != 0:
                return True
        return False

def openDoor(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "D":
                map[i][j] = "E"
                pygame.mixer.Sound.play(doorOpen)
                return

def openColorDoor(map, color):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if color == "RED":
                if map[i][j] == "R":
                    map[i][j] = "S"
                    pygame.mixer.Sound.play(colorDoorOpen)
            if color == "GREEN":
                if map[i][j] == "G":
                    map[i][j] = "S"
                    pygame.mixer.Sound.play(colorDoorOpen)
            if color == "BLUE":
                if map[i][j] == "F":
                    map[i][j] = "S"
                    pygame.mixer.Sound.play(colorDoorOpen)

class Game:
    def __init__(self, screen):
        self.gameStarted = False
        self.gamePaused = False
        self.screen = screen
        self.objects = []
        self.map = []
        self.game_state = GameState.NONE
        self.lvl = 0
        self.camera = [0, 0]
        
    def set_up(self, lvl):
        if lvl == 0:
            pygame.mixer.music.load("audio/lobbyMusic.wav")
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.load("audio/bgMusic.wav")
            pygame.mixer.music.play(-1)
        if lvl == 1:
            self.gameStarted = True
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        self.game_state = GameState.RUNNING
        self.load_map(f"LV{lvl}")

    def update(self):
        #clear screen first
        self.screen.fill(config.BLACK)
        #print("update")
        #handle all events related to the object
        self.handle_events()

        self.render_map(self.screen)
        
        #every object in objects should have a render function
        for object in self.objects:
            object.render(self.screen, self.camera)

        if not hasBlackTiles(self.map):
            openDoor(self.map)

    def handle_events(self):
        if self.gamePaused:
            self.player.camo_player()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            leftClick = pygame.mouse.get_pressed()[0]
            mousePos = pygame.mouse.get_pos() # monitor mouseX and mouseY
            mouseX = mousePos[0]
            mouseY = mousePos[1]
            keys = pygame.key.get_pressed() # monitor all keystrokes
            if self.gameStarted and (keys[pygame.K_ESCAPE] and not self.gamePaused):
                self.gamePaused = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("audio/pauseMusic.wav")
                pygame.mixer.music.play(-1)
            elif self.gameStarted and (keys[pygame.K_ESCAPE] and self.gamePaused):
                self.gamePaused = False
                self.player.change_sprite(0)
                pygame.mixer.music.stop()
                pygame.mixer.music.load("audio/bgMusic.wav")
                pygame.mixer.music.play(-1)
            elif not self.gamePaused and (keys[pygame.K_w] or keys[pygame.K_UP]): #up
                self.player.change_sprite(3)
                self.move_unit(self.player, [0, -1])
            elif not self.gamePaused and (keys[pygame.K_a] or keys[pygame.K_LEFT]): #left
                self.player.change_sprite(2)
                self.move_unit(self.player, [-1, 0])
            elif not self.gamePaused and (keys[pygame.K_s] or keys[pygame.K_DOWN]): #down
                self.player.change_sprite(0)
                self.move_unit(self.player, [0, 1])
            elif not self.gamePaused and (keys[pygame.K_d] or keys[pygame.K_RIGHT]): #right
                self.player.change_sprite(1)
                self.move_unit(self.player, [1, 0])
            if not self.gamePaused and keys[pygame.K_z]:
                self.player.camo_player()
                self.set_up(5)
            if not self.gamePaused and keys[pygame.K_c]:
                openDoor(self.map)
                openColorDoor(self.map, "RED")
                openColorDoor(self.map, "GREEN")
                openColorDoor(self.map, "BLUE")
            xInBounds = (mouseX > 131 and mouseX < 488)
            yInReset = (mouseY > 188 and mouseY < 291)
            yInExit = (mouseY > 347 and mouseY < 450)
            if self.gamePaused and ((xInBounds and yInReset and leftClick == 1) or keys[pygame.K_r]):
                self.gamePaused = False
                self.player.camo_player()
                self.set_up(self.lvl)
            if self.gamePaused and ((xInBounds and yInExit and leftClick == 1) or keys[pygame.K_q]):
                self.game_state = GameState.ENDED
            if not self.gameStarted:
                self.player.camo_player()
            if not self.gameStarted and keys[pygame.K_SPACE]:
                pygame.mixer.Sound.play(doorOpen)
                pygame.mixer.music.stop()
                time.sleep(0.5)
                self.lvl += 1
                self.set_up(self.lvl)
    
    def load_map(self, file_name):
        self.map = []
        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)
    
    def render_map(self, screen):
        if self.gamePaused:
            pauseImg = pygame.transform.scale(pygame.image.load("sprites/Pause.png"), (600, 600))
            screen.blit(pauseImg, (0, 0))
            return

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
        useJump = False
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]
        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return
        if new_position[1] < 0 or new_position[1] > (len(self.map) - 1):
            return
        if self.map[new_position[1]][new_position[0]] == "W":
            return
        if self.map[new_position[1]][new_position[0]] == "R":
            return
        if self.map[new_position[1]][new_position[0]] == "G":
            return
        if self.map[new_position[1]][new_position[0]] == "F":
            return
        if self.map[new_position[1]][new_position[0]] == "_" or self.map[new_position[1]][new_position[0]] == "-":
            return
        if self.map[new_position[1]][new_position[0]] == "H":
            return
        if self.map[new_position[1]][new_position[0]] == "D":
            return
        if self.map[new_position[1]][new_position[0]] == "B":
            pygame.mixer.Sound.play(tileSwitch)
            self.map[new_position[1]][new_position[0]] = "X" #swap b for w
        elif self.map[new_position[1]][new_position[0]] == "X":
            pygame.mixer.Sound.play(tileSwitch)
            self.map[new_position[1]][new_position[0]] = "B" #swap w for b
        if self.map[new_position[1]][new_position[0]] == "J":
            useJump = True
        if self.map[new_position[1]][new_position[0]] == "C":
            self.map[new_position[1]][new_position[0]] = "H"
            pygame.mixer.Sound.play(tileBreak)
        if self.map[new_position[1]][new_position[0]] == "0":
           openColorDoor(self.map, "RED")
        if self.map[new_position[1]][new_position[0]] == "1":
           openColorDoor(self.map, "GREEN")
        if self.map[new_position[1]][new_position[0]] == "2":
           openColorDoor(self.map, "BLUE")
        if self.map[new_position[1]][new_position[0]] == "K":
            pygame.mixer.music.stop()
            doorOpen(self.map)
            pygame.mixer.Sound.play(diamondGet)
            time.sleep(9)
            self.map[new_position[1]][new_position[0]] = "S"
            pygame.mixer.music.stop()
            pygame.mixer.music.load("audio/bgMusic.wav")
            pygame.mixer.music.play(-1)
        if self.map[new_position[1]][new_position[0]] == "E":
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(winSound)
            time.sleep(5)
            self.lvl += 1
            self.player.camo_player()
            self.set_up(self.lvl)

        if useJump:
            new_position[0] += position_change[0] * 2
            new_position[1] += position_change[1] * 2
            if self.map[new_position[1]][new_position[0]] == "W":
                return
            if self.map[new_position[1]][new_position[0]] == "R":
                return
            if self.map[new_position[1]][new_position[0]] == "G":
                return
            if self.map[new_position[1]][new_position[0]] == "F":
                return
            if self.map[new_position[1]][new_position[0]] == "D":
                return
            if self.map[new_position[1]][new_position[0]] == "_" or self.map[new_position[1]][new_position[0]] == "-":
                return
            if new_position[0] < 0 or new_position[1] < 0:
                return
            pygame.mixer.Sound.play(jumpSound)
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
            
            
