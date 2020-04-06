def createMatrix(r,c):
    matrix = [[ 0 for i in range(r)] for j in range(c)]
    return matrix

def fillMatrix(matrix):
    matrix = [[2, 1, -3, -4, 5], [0, 6, 3, 4, 1], [2, -2, -1, 4, -5], [-3, 3, 1, 0, 3]]
    return matrix

def findContiguousSum(matrix):
    gl,tl,gu,gd,gr,gmax = (0,0,0,0,0,0)
    for k in range(c):
        sum_matrix = [0 for i in range(len(matrix))]
        current_matrix = [0 for i in range(len(matrix))]
        tl=k
        for j in range(k,c):
            for i in range(r):
                sum_matrix[i] += matrix[i][j]
                current_matrix[i] = matrix[i][j]
            tu,td,max = kadanesAlgo(sum_matrix)
            tu1,td1,max1 = kadanesAlgo(current_matrix)

            if max>max1:
                if max>gmax:
                    gu=tu
                    gd=td
                    gl=tl
                    gr=j
                    gmax=max
            elif max1>max:
                if max1>gmax:
                    gu=tu1
                    gd=td1
                    gl=tl
                    gr=j
                    gmax=max
                else:
                    sum_matrix = current_matrix
                    tl = j
    print (gl,gr,gu,gd,gmax)
def kadanesAlgo(array):
    max=array[0]
    gup=0
    gdown=0
    sum=0
    tup=0
    for i in range(len(array)):
        sum+=array[i]
        if sum<array[i]:
            tup=i
            sum = array[i]
        if sum>max:
            gup=tup
            gdown=i
            max=sum
    return gup,gdown,max
        
    
            
    
if __name__ == "__main__":

    r = int(input("Enter the row size: "))
    c = int(input("Enter the column size: "))
    matrix = createMatrix(r,c)
    matrix = fillMatrix(matrix)
    print(matrix)
    findContiguousSum(matrix)
    
    
