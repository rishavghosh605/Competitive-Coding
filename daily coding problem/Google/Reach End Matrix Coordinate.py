from queue import Queue

class Matrix():
    pass

def create_matrix(matrix):
    pass

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

if __name__=="__main__":

    M=int(input("Enter the row size of the matrix: "))
    N=int(input("Enter the column size of the matrix: "))

    matrix=Matrix(M,N)
    create_matrix(matrix)
    find_steps_to_end(start,end,matrix)
    
