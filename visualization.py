from mazelib import Maze
from mazelib.generate.BacktrackingGenerator import BacktrackingGenerator
import pygame

pygame.init()
clock = pygame.time.Clock()


WIDTH = 1400
HEIGHT = 1400
run = True

WIN = pygame.display.set_mode((WIDTH,HEIGHT))



import random


"""
    1. Randomly choose a starting cell.
    2. Randomly choose a wall at the current cell and open a passage through to any random adjacent
        cell, that has not been visited yet. This is now the current cell.
    3. If all adjacent cells have been visited, back up to the previous and repeat step 2.
    4. Stop when the algorithm has backed all the way up to the starting cell.
"""

def GenMaze(width,height):
    grid = []
    for i in range(height):
        grid.append([1] * width)

    return grid


def PrintGrid(grid):
    for row in grid:
        print(row)


def GetNeighbours(row,col,grid):
    arr = []


    if col + 2 < len(grid[row]):
        if grid[row][col+2] == 1:
            arr.append((row,col+2))

    if col - 2 > 0:
        if grid[row][col-2] == 1:
            arr.append((row,col-2))


    if row - 2 > 0:
        if grid[row-2][col] == 1:
            arr.append((row-2,col))

    if row + 2 < len(grid):
        if grid[row+2][col] == 1:
            arr.append((row+2,col))

    return arr


grid = GenMaze(200,200)


Crow = random.randint(0,len(grid))
Ccol = random.randint(0,len(grid[0]))


grid[Crow][Ccol] = 0

track = [(Crow,Ccol)]


    


while(run):
    clock.tick()
    WIN.fill((0,0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if track:
        (Crow,Ccol) = track[-1]
        
        ns = GetNeighbours(Crow,Ccol,grid)
        
        if len(ns) != 0:
            Nrow,Ncol = random.choice(ns)
            grid[Nrow][Ncol] = 0
            grid[(Nrow + Crow) // 2][(Ncol + Ccol) // 2] = 0

            

            track.append((Nrow, Ncol))
        else:
            track.pop()

    



    


    for y,row in enumerate(grid):
        for x,col in enumerate(row):
            if col == 1:
                pygame.draw.rect(WIN,(0,0,0),pygame.Rect(x*7,y*7,7,7))
            if col == 0:
                pygame.draw.rect(WIN,(255,255,255),pygame.Rect(x*7,y*7,7,7))

    

    
    
    pygame.display.update()