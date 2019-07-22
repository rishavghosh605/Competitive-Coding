                
"""
Leetcode Description:
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
"""

"""
Daily Coding Problem Description:
This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

"""
import numpy as np
def createGridOfLife(grid):
    n=int(input("Enter the number of cells that are alive: "))
    for i in range(n):
        liveCoordinateX,liveCoordinateY=tuple(map(int,input("Enter the x and y coordinate for the live cell: ").split(' ')))
        grid[liveCoordinateX,liveCoordinateY]='*'
    return grid

def countNeighbours(grid,X,Y):
    aliveNeighbours=0
    k,j=(X,Y)
    
    #Creating the row and column vectors to check the neighbours of the given cell
    r=[-1,0,1,-1,1,1,0,-1]
    c=[-1,-1,-1,0,0,1,1,1]
    for i in range(len(r)):
        if X+r[i] >= 0 and X+r[i] < N and Y+c[i] >= 0 and Y+c[i] < M:
            aliveNeighbours+=1 if grid[X+r[i],Y+c[i]] in ('*','-')  else 0
            
    return aliveNeighbours
    
def decideCellLife(aliveNeighbours,cell):

    if cell=='*':
        if aliveNeighbours<2 or aliveNeighbours>3:
            return '-'
        
    elif cell=='.':
        if aliveNeighbours==3:
            return '+'
        
    return cell        
        
    
    
def playGameOfLife(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            aliveNeighbours=countNeighbours(grid,i,j)
            
            grid[i,j]=decideCellLife(aliveNeighbours,grid[i,j])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='+':
                grid[i][j]='*'
            elif grid[i][j]=='-':
                grid[i][j]='.'
            

    return grid
            
            
            


if __name__=="__main__":

    M=int(input("Enter the number of columns of the grid: "))
    N=int(input("Enter the number of rows of the grid: "))
    grid=[['.']*M]*N
    grid=np.array(grid)
    print(grid)
    grid=createGridOfLife(grid)
    print(grid)
    steps=int(input("Enter the number of steps for which it can run: "))
    for step in range(steps):
        grid=playGameOfLife(grid)
        print("After step ",step+1,"the grid is: \n",grid)
    
               
        
