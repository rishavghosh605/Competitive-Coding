"""
This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.

"""

def countTours(curr,chessboard):

    next_moves=findMoves()
    for move in next_moves:
        if isSafe(curr,move,chessboard):
            if countTours(move,chessboard):
                return True
    return False
            
    
if __name__=="__main__":

    N=int(input("Enter the size of the matrix"))
    chessboard=[[0 for i in range(N)] for j in range (N)]
    print(countTours((0,0),chessboard))
