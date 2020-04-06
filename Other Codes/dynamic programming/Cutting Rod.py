#5 122


def findMatrixDimensions(n,d):
    return (len(d),n+1)

def findMaximumSum(n,d,ll):
    r,c = findMatrixDimensions(n,d)
    matrix = [[0 for i in range(c)] for i in range(r)]
    print(d,ll)
    for i in range(r):
        for j in range(c):
            if i>0:
                matrix[i][j] = max(d[ll[i]]+matrix[i][j-ll[i]],matrix[i-1][j]) if (j>=ll[i]) else matrix[i-1][j]
            else:
                matrix[i][j] = d[ll[i]]+matrix[i][j-ll[i]] if j-ll[i]>=0 else 0
    divisions=findDivisions(matrix,n,d,ll)
    return matrix[r-1][c-1],divisions

def findDivisions(matrix,n,d,ll):
    r,c = findMatrixDimensions(n,d)
    i=r-1
    j=c-1
    divisions= list()
    while(not matrix[i][j]==0):
        print(divisions)
        if matrix[i-1][j] == matrix[i][j] and i>0:
            i=i-1
        elif matrix[i][j-ll[i]] + d[ll[i]] == matrix[i][j] and j-ll[i]>=0:
            j=j-ll[i]
            divisions.append(ll[i])
    return divisions[::-1]
if __name__ == "__main__":

    n=int(input("Enter the sum you want to find: "))
    l = list(map(int,input("Enter the key value pairs for the weights: ").split()))
    #Inializing a length list that maps to the dict
    ll = list()
    d={}
    for i in range(0,len(l),2):
        d[l[i]] = l[i+1]
        ll.append(l[i])
    max_sum,divisions = findMaximumSum(n,d,ll)
    print("The Max Sum is: ",max_sum)
    print("The divisions are: ",divisions)
