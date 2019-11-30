from queue import Queue

class Matrix():
    def __init__(self,M=0,N=0):
        self.M=M
        self.N=N
        self.matrix=[[0 for j in range(N)]for i in range(M)]

    def print(self):
        print(self.matrix)

    def get_rows(self):
        return self.M

    def get_columns(self):
        return self.N
    
   
    
        

def find_steps_to_end(start,end,matrix):
    visited_matrix=Matrix(M,N)
    q=Queue()
    q.put(start)
    neighbours=1
    next_neighbours=0
    count=1
    while(not q.empty()):
        node=q.pop()
        if(node==end):
            return count
        neighbors_list=find_neighbours(node,visited_matrix)
        next_neighbours+=len(neighbors_list)
        neighbors-=1;
        if(neighbors==0):
            count+=1
            neighbors=next_neighbours
def find_neighbours(node,visited_matrix):

    dr=[-1,0,+1]
    dc=[-1,0,+1]
    neighbors_list=list()
    for i in dr:
        for j in dc:
            if not (i==0 and j==0):
                if (isSafe(node[0]+r,node[1]+j)):
                    neighbors_list.append((node[0]+r,node[1]+j))
    return neighbors_list

if __name__=="__main__":

    M=int(input("Enter the row size of the matrix: "))
    N=int(input("Enter the column size of the matrix: "))

    matrix=Matrix(M,N)
    matrix.print()
    start=tuple(map(int,input("Enter the start coordinate of the matrix: ").split()))
    end=tuple(map(int,input("Enter the end coordinate of the matrix: ").split()))
    #find_steps_to_end(start,end,matrix)
    visited_matrix=Matrix(M,N)
    print(find_neighbours(start,visited_matrix))
    
    
    
