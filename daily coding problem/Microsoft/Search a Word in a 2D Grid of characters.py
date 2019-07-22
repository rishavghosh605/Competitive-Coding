"""
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word,
write a function that returns whether the word can be
found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
 
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
"""

def create_matrix(matrix):
 
    l=input("Enter the words: ").split(' ')
    count=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j]=l[count]
            count+=1

def find_word(word,matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j]==word[0]
            
            if checkForWord(word,matrix,i,j):
                return True

def checkForWord(word,matrix,row,column):

    topDown = row + len(word)
    leftRight = column + len(word)
    flag=0
    if topDown<N:
        
        for i in range(row,topDown):
            if matrix[i][column] != word[i%row if row>0 else i]:
                flag+=1
                break
            
    if leftRight < N:
        
        for j in range(column,leftRight):
            if matrix[row][j] != word[j%column if column>0 else j]:
                flag+=1
                break
    if flag == 2:
        return False
    return True
        

if __name__=="__main__":

    # Stores length of matrix
    N=int(input("Enter size of matrix: "))
    word=input("Enter the word to be found: ")
    matrix=[['' for i in range(N)] for j in range(N)]
    create_matrix(matrix)
    print(matrix)
    print(find_word(word,matrix))
    
