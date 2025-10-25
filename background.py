import pygame
### Screen Properties
TILE_SIZE = 32
sprite_sheet_size = (TILE_SIZE * 32, TILE_SIZE*16)
dungeon_floors_walls = pygame.image.load('Tiles-SandstoneDungeons.png')
dungeon_walls = pygame.image.load('Tiles-Door-packs.png')
WIDTH = 800
HEIGHT = 608
screen = pygame.display.set_mode((WIDTH, HEIGHT))
misc = pygame.image.load('Tiles-Props-pack.png').convert_alpha()
misc.set_colorkey((0,0,0,))


def get_tile(sheet, x, y):
    '''slices a single tile from the sheet
        Args: 
            sheet(pygame.Surface): The sprite sheet image
            x(int): the column index of the tile
            y(int): the row index of the tile
            
            Returns:
            pygame.Surface: a new surface containing the extracted tile
            '''
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


decorations = []
sheet_width3 = misc.get_width()
sheet_height3 = misc.get_height()
cols3 = sheet_width3 // TILE_SIZE
rows3 = sheet_width3 // TILE_SIZE
for y in range (rows3):
    for x in range (cols3):
        decorations.append(get_tile(misc,x,y))

