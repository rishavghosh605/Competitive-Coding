perms=[]
def printAllPermutations(l):

    visited_list=[0 for i in range(len(l))]
    findAllPermutations(l,visited_list,"")
    
def findAllPermutations(l,visited_list,p):

    if len(p)==len(l):
        perms.append(p)
        return

    for i in range(len(l)):
        if visited_list[i]==0:
            visited_list[i]=1
            findAllPermutations(l,visited_list,p+l[i])
            visited_list[i]=0
    return
    

if __name__=="__main__":

    s=input("Enter the list of digits: ")
    l=[]
    for i in s:
        l.append(i)
    printAllPermutations(l)
    print("The parmutations are:\n",perms)
    print("No. of permutations are:\n",len(perms))
