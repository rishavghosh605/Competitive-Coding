"""
This problem was asked by Dropbox.

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

Implement an efficient sudoku solver.
"""

def createSudoku(grid):
    n=int(input("Enter total number of assigned "))

def findInstance(grid,instance):
    for i in range(9):
        for j in range(9):
            
            if grid[i,j]==0:
                instance[0]=i
                instance[1]=j
                
                return True
    return False
# i is the num we are setting at the coordinates of instance
def rowSafe(grid,instance,num):
    
    for column in range(len(grid[0])):
        
        if grid[instance[0],column]==num:
            return False
    return True

def columnSafe(grid,instance,num):
    
    for row in range(len(grid)):
        #print(grid[row,instance[1]])
        if grid[row,instance[1]]==num:
            return False
    return True

def subGridSafe(grid,instance,num):
    
    for i in range(3):
        for j in range(3):
            row=(instance[0]-instance[0]%3)+i
            column=(instance[1]-instance[1]%3)+j
            if grid[row,column]==num:
                return False
    return True
    
def isSafe(grid,instance,num):

    condition1=rowSafe(grid,instance,num)

    condition2=columnSafe(grid,instance,num)

    condition3=subGridSafe(grid,instance,num)

    if condition1 and condition2 and condition3:
        return True
    return False
    
def solveSudoku(grid):
    instance=[0,0]
    
    if(not findInstance(grid,instance)):
        return True
    
    for num in range(1,len(grid)+1):
        # checking if location is safe with isSafe
        if(isSafe(grid,instance,num)):
            # A tentative assignment is made
            grid[instance[0],instance[1]]=num
            if(solveSudoku(grid)):
                return True

        grid[instance[0],instance[1]]=0
            
    return False
    

if __name__=="__main__":

    import numpy as np
    N=9
    grid=np.array([[0]*N]*N)
    #createSudoku(grid)
    grid=np.array([[3,0,6,5,0,8,4,0,0], 
                   [5,2,0,0,0,0,0,0,0], 
                   [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]] )
    if(solveSudoku(grid)):
        print("The sudoku is:\n",grid)
    else:
        print("No solution exists")
    

    
































        
    
    
