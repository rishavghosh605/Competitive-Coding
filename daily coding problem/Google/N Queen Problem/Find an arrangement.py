"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns a possible arrangement of the board where N queens can be placed on the board
without threatening each other, i.e. no two queens share the same row, column,
or diagonal.

"""
import numpy as np
def solveNQueens(N):
    column=0
    arrangement=[]
    chessboard,arrangement=findNQueenArrangement(N,column,arrangement)
    
    print("The arrangement of the queens:",arrangement)
    return chessboard

def findNQueenArrangement(N,column,arrangement):

    if column==N:
        chessboard=np.array([[0]*N]*N)
        for queen_row,queen_col in arrangement:
            chessboard[queen_row,queen_col]=1
        return chessboard,arrangement

    for row in range(N):

        if isSafe(row,column,arrangement):
            arrangement.append((row,column))
            chessboard,arrangement=findNQueenArrangement(N,column+1,arrangement)

            if chessboard!=[]:
                return chessboard,arrangement
            arrangement=arrangement[:-1]

    return ([],arrangement)
            
    
def isSafe(row,column,arrangement):

    for qr,qc in arrangement:
        if row == qr or row == qr+(column-qc) or row == qr-(column-qc) :
            return False
    return True


if __name__=="__main__":

    N = int(input("Enter the chess-board size: "))
    chessboard=solveNQueens(N)
    print("The chessboard will look like: ")
    print("\n",chessboard)
