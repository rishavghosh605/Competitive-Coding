def createSubsequenceMatrix(s1,s2):

    matrix=[[0 for j in s1] for i in s2]
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s1[j]==s2[i]:
                if i==0 or j==0:
                    matrix[i][j]=1
                else:
                    matrix[i][j]=1+matrix[i-1][j-1]
            else:
                if j==0 and i!=0:
                    matrix[i][j]=matrix[i-1][j]
                elif i==0 and j!=0:
                    matrix[i][j]=matrix[i][j-1]
                else:
                    matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])
    return matrix

def findSubsequence(matrix,s1,s2):

    l=matrix[len(matrix)-1][len(matrix[0])-1]
    s=_findSubsequence(matrix,s1,s2)
    return l,s

def _findSubsequence(matrix,s1,s2):

    s=""
    i=len(matrix)-1
    j=len(matrix[0])-1
    while True:
        if j>0 and matrix[i][j]==matrix[i][j-1]:
            j=j-1
        elif i>0 and matrix[i][j]==matrix[i-1][j]:
            i=i-1
        elif i>0 and j>0 and (matrix[i][j]==1+matrix[i-1][j-1]):
            s+=s1[j]
            i=i-1
            j=j-1
        else:
            s+=s1[j] if matrix[i][j]>0 else ""
            break
    return s[::-1] if s!="" else "No subsequence found"
            
if __name__=="__main__":

    s1=input("First string: ")
    s2=input("Second string: ")

    matrix=createSubsequenceMatrix(s1,s2)
    for i in range(len(matrix)):
        print(matrix[i])
    l,s=findSubsequence(matrix,s1,s2)
    print("Length: ",l,"Subsequence: ",s)
