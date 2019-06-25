"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number
of possible arrangements of the board where N queens can be placed on the board
without threatening each other, i.e. no two queens share the same row, column,
or diagonal.

"""
import numpy as np
def solveNQueens(N):
    column=0
    arrangement=[]
    count,arrangement=findNQueenArrangements(N,column,arrangement)
    return count

def findNQueenArrangements(N,column,arrangement):
    if column==N:
        return 1,arrangement
    total_count=0
    for row in range(N):

        if isSafe(row,column,arrangement):
            count=0
            arrangement.append((row,column))
            count,arrangement=findNQueenArrangements(N,column+1,arrangement)

            total_count+=count
            arrangement=arrangement[:-1]

    return (total_count,arrangement)
            
    
def isSafe(row,column,arrangement):

    for qr,qc in arrangement:
        if row == qr or row == qr+(column-qc) or row == qr-(column-qc) :
            return False
    return True


if __name__=="__main__":

    N = int(input("Enter the chess-board size: "))
    count=solveNQueens(N)
    print("Total no. of arrangments: ",count)
