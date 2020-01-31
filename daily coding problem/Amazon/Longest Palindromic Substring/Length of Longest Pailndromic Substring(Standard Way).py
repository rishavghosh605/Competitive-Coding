def recursive_approach(s):
    print(s)
    if len(s)==1:
        return 1
    
    elif s[0]==s[len(s)-1]:
        return recursive_approach(s[1:len(s)-1])+2 if len(s)!=2 else 2
    else:
        return max(recursive_approach(s[1:len(s)]),recursive_approach(s[0:len(s)-1]))

def dynamic_approach(s):
    l=len(s)
    matrix=[[0 for i in range(l)] for i in range(l)]
    for i in range(l):
        matrix[i][i]=1

    for i in range(1,l):
        for j in range(0,l-i):
            matrix[j][j+i]=matrix[j+1][j+i-1]+2 if s[j]==s[j+i] else max(matrix[j][j+i-1],matrix[j+1][j+i])
    for i in range(l):
        print(matrix[i])
    return matrix[0][len(s)-1]

if __name__== "__main__":

    s=input("Enter a string: ")
    k=recursive_approach(s)
    print("Length from recursive approach: ",k)
    k=dynamic_approach(s)
    print("Length from dynamic approach: ",k)
