from queue import Queue
import numpy as np
class Matrix():
    def __init__(self,M=0,N=0):
        self.M=M
        self.N=N
        self.matrix=np.array([[0 for j in range(self.N)] for i in range(self.M)])
    def print(self):
        print(self.matrix)
        
    

def create_matrix(matrix):
    pass

def find_steps_to_end(start,end,matrix):
    visited_matrix=Matrix(M,N)
    q=Queue()
    q.put(start)
    neighbors=1
    next_neighbors=0
    count=0
    while(not q.empty()):
        node=q.get()
        if(node==end):
            return count
        neighbors_list=find_neighbors(node,visited_matrix)
        next_neighbors+=len(neighbors_list)
        neighbors-=1;
        for i in neighbors_list:
            q.put(i)
        if(neighbors==0):
            print(node)
            count+=1
            neighbors=next_neighbors
            next_neighbors=0
    return count
def find_neighbors(node,visited_matrix):

    dr=[-1,0,+1]
    dc=[-1,0,+1]
    neighbors_list=list()
    for i in dr:
        for j in dc:
            if not (i==0 and j==0):
                if (isSafe(node[0]+i,node[1]+j,len(visited_matrix.matrix),len(visited_matrix.matrix[0]))):
                    neighbors_list.append((node[0]+i,node[1]+j))
    return neighbors_list

def isSafe(i,j,r,c):

    if i<0 or i>r-1 or j<0 or j>c-1:
        return False
    return True

    
    

if __name__=="__main__":

    M=int(input("Enter the row size of the matrix: "))
    N=int(input("Enter the column size of the matrix: "))

    matrix=Matrix(M,N)
    matrix.print()
    start=tuple(map(int,input("Enter the start coordinate of the matrix: ").split()))
    end=tuple(map(int,input("Enter the end coordinate of the matrix: ").split()))
    
    visited_matrix=Matrix(M,N)
    

    #create_matrix(matrix)
    print(find_steps_to_end(start,end,matrix))
    
