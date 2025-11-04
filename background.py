##########!!!!!!! MAKE INTO CLASS FOR EFFICIENCY
import pygame
from util_params import *
### Screen Properties
background = pygame.Surface((WIDTH, HEIGHT))


 #make background frome tiles pulled from sprite sheet
TILE_SIZE = 32
#define separate sprite sheets
dungeon_floors_walls = pygame.image.load('building blocks/Tiles-SandstoneDungeons.png')
dungeon_walls = pygame.image.load('building blocks/Tiles-Door-packs.png')

def get_tile(sheet, x, y):
#creat new blank Surface for the tile
    tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
#copy the tile from the sprite sheet to the new surface
    tile.blit(sheet, (0,0), (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    return tile
#create list of all tiles
floors = []
sheet_width = dungeon_floors_walls.get_width()
sheet_height = dungeon_floors_walls.get_height()
cols = sheet_width // TILE_SIZE
rows = sheet_height // TILE_SIZE
for y in range (rows):
    for x in range (cols):
        floors.append(get_tile(dungeon_floors_walls, x, y))

doors = []
sheet_width2 = dungeon_walls.get_width()
sheet_height2 = dungeon_walls.get_height()
cols2 = sheet_width2 // TILE_SIZE
rows2 = sheet_width2 // TILE_SIZE
for y in range (rows2):
    for x in range (cols2):
        doors.append(get_tile(dungeon_walls,x,y))

basic_floor = floors[1]
wall_bottom = floors[55]
wall_top = floors[19]
wall_left = floors[18]
wall_right = floors[20]
right_corner = floors[27]
left_corner = floors[29]
blank = floors[62]
torches = pygame.image.load('building blocks/items/torch_4.png')
def make_background():
    #place basic floor tiles 
    for x in range (0, WIDTH, TILE_SIZE):
        for y in range(0,HEIGHT, TILE_SIZE):
            background.blit(basic_floor, (x,y))
    #place wall at bottom of the screen
    for x in range(0, WIDTH, TILE_SIZE):
        background.blit(wall_bottom,(x,HEIGHT-58))
    #place wall at top of the screen
    for x in range(0, WIDTH, TILE_SIZE):
        background.blit(wall_top, (x,0))
    #layer right wall on top of bottom and top walls
    for y in range(0, HEIGHT, TILE_SIZE):
        background.blit(wall_right,(x,y))
    #layer left wall on top of bottom and top walls
    for y in range(0, HEIGHT, TILE_SIZE):
        background.blit(wall_left, (0,y))
    #place blank black boxes at bottom of screen 
    for x in range(0,WIDTH, TILE_SIZE):
        for y in range(HEIGHT-54, HEIGHT, TILE_SIZE):
            background.blit(blank,(x,y))
    # place torches at equal increment inside of enclosure
    for x in range(64, WIDTH - 64, 32):
        for y in range (64, HEIGHT - 64, 32 ):
            background.blit(torches,(x, y))

    return background
   