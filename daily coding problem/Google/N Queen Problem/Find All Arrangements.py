"""
This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number
of possible arrangements of the board  as well as all the arrangements where N queens can be placed on the board
without threatening each other, i.e. no two queens share the same row, column,
or diagonal.

"""
import numpy as np
def solveNQueens(N):
    column=0
    count=[0]
    arrangement=[]
    chessboards,arrangement=findNQueenArrangements(N,column,arrangement,count)
    print("Total no. of arrangments: ",count[0])
    return chessboards

def findNQueenArrangements(N,column,arrangement,count):
    chessboard_matrix=[]
    if column==N:
        chessboard=np.array([[0]*N]*N)
        for queen_row,queen_col in arrangement:
            chessboard[queen_row,queen_col]=1

        count[0]+=1
        return chessboard,arrangement

    for row in range(N):

        if isSafe(row,column,arrangement):

            arrangement.append((row,column))
            chessboard,arrangement=findNQueenArrangements(N,column+1,arrangement,count)

            if chessboard!=[]:
                chessboard_matrix.append(chessboard)
            arrangement=arrangement[:-1]

    return (chessboard_matrix,arrangement)
            
    
def isSafe(row,column,arrangement):

    for qr,qc in arrangement:
        if row == qr or row == qr+(column-qc) or row == qr-(column-qc) :
            return False
    return True


if __name__=="__main__":

    N = int(input("Enter the chess-board size: "))
    chessboards=solveNQueens(N)
    print("The chessboard arrangements are as folllows:")
    for chessboard in chessboards:
        print("\n",chessboard)
