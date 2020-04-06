def sortStack(s1,s2):

    if(len(s1)==0):
        return
    temp=s1.pop()
    s1,s2 = sortStackByInsert(temp,s1,s2)
    return sortStack(s1,s2)

def sortStackByInsert(temp,s1,s2):

    
    if(len(s2)>0 and temp<s2[-1]):
        s1.append(s2.pop())
        sortStackByInsert(temp,s1,s2)
    else:
        s2.append(temp)
    return s1,s2
        


if __name__=="__main__":

    #n=int(input("Enter the number of values in the stack: "))
    s1=[4,15,1,7,9]
    s2=[]
    '''
    for i in range(n):
        s1.append(int(input("Enter a number: ")))'''
    print("Unsorted: ",s1)
    sortStack(s1,s2)
    print("Sorted: ",s2)
    
