'''
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''
import queue
import numpy as np
class Matrix():
    def __init__(self,M,N):

        self.rows=M
        self.columns=N
        self.matrix=np.array([['f']*self.columns]*self.rows)
        
    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def get_matrix(self):
        return self.matrix
    
    def set_visited(self,r,c):
        self.matrix[r,c]='t'

    def is_node_valid(self,r,c):

        if r < 0 or r >= self.rows or c < 0 or c >= self.columns:
            return False
        elif self.matrix[r,c]=='t':
            print(r,c)
            return False
        return True

def create_matrix(maze):

    n=int(input("Enter the number of coordinates where the maze is blocked: "))
    for i in range(n):
        r = int(input("Enter the row: "))
        c= int(input("Enter the column: "))
        maze.set_visited(r,c)

    print(maze.get_matrix())
        
    
   

def find_steps_to_end(start,end,maze):
    # Initializing the queues
    rq = queue.Queue()
    cq = queue.Queue()
    #Variables to track the number of steps taken
    move_count=0
    nodes_left_in_layer=1
    nodes_in_next_layer=0

    # The direction vectors to go up, down,left and right
    dr=[-1,+1,0,0]
    dc=[0,0,-1,+1]

    #To check if the destination is reached or not:
    reached_end=False

    # A visited matrix is created to keep track whther the node at position (i,j) has been reached or not
    visited=Matrix(maze.get_rows(),maze.get_columns())


    # The start point is inserted into the queue and marked visited
    r = start[0]
    c= start[1]
    rq.put(r)
    cq.put(c)
    visited.set_visited(r,c)

    # Now we start a while loop and continue until either we reach the destination or the queue becomes empty
    while(not rq.empty()):
        
        # Dequeue and get a row and column value to check its adjacent cells
        r=rq.get()
        c=cq.get()
        print("This layer:",r,c,nodes_left_in_layer,nodes_in_next_layer)
        # Check if destination is reached
        if (r,c) == end:
            reached_end=True
            break

        # We add valid neighbours and update the queue and visited matrix with the adjacent nodes of the current node
        for i in range(len(dr)):
            if maze.is_node_valid(r+dr[i],c+dc[i]):
                if visited.is_node_valid(r+dr[i],c+dc[i]):
                    rq.put(r+dr[i])
                    cq.put(c+dc[i])
                    visited.set_visited(r+dr[i],c+dc[i])
                    print("Next layer:",r+dr[i],c+dc[i])
                    nodes_in_next_layer+=1        

        # We check certain variables to update the number of moves made
        nodes_left_in_layer -= 1
        if nodes_left_in_layer==0:
            nodes_left_in_layer=nodes_in_next_layer
            nodes_in_next_layer=0
            move_count+=1
            
    if reached_end == True:
        return move_count  
    return "Not Found"


if __name__=="__main__":

    M=int(input("Enter the row size of the matrix: "))
    N=int(input("Enter the column size of the matrix: "))
    maze=Matrix(M,N)
    create_matrix(maze)

    start = tuple(map(int,input("Enter the starting coordinates: ").split(' ')))
    end = tuple(map(int,input("Enter the ending coordinates: ").split(' ')))
    print(find_steps_to_end(start,end,maze))
    
