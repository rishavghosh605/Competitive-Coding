def printRight(s,matrix):
    n=len(matrix[0])
    m=len(matrix)
    for i in range(s,n-s):
        print(matrix[s][i])

    

def printDown(s,matrix):
    n=len(matrix[0])
    m=len(matrix)
    for i in range(s,m-s):
        if i !=s:
            print(matrix[i][n-s-1])
    
    

def printLeft(s,matrix):
    n=len(matrix[0])
    m=len(matrix)
    count=0
    for i in range(s,n-s):
        if i!= s:
            print(matrix[m-s-1][n-s-1-count])
        count+=1

    

def printUp(s,matrix):
    
    n=len(matrix[0])
    m=len(matrix)
    count=0
    for i in range(s,m-s):
        if i != s and i!=m-s-1:
            print(matrix[m-s-1-count][s])
        count+=1

    
    
def printSpiralMatrix(matrix):

    s=0
    n=len(matrix[0])
    while s<(n)//2:
        printRight(s,matrix)
        printDown(s,matrix)
        printLeft(s,matrix)
        printUp(s,matrix)
        
        s+=1
        

if __name__=="__main__":

    #n=int(input("Enter the size of the matrix: "))
    #matrix = list(map(int,input("Enter the integers")))
    matrix=[[0 for i in range(5)] for j in range(4)]
    c=1
    for i in range(4):
        for j in range(5):
            matrix[i][j]=c
            c+=1
    import numpy as np
    print("The matrix",np.array(matrix))
    print("The spiral display will be:")
    printSpiralMatrix(matrix)
    
    
