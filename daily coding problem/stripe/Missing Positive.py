'''This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.'''


def segregate(l):
    j=0
    for i in range(len(l)):
        if int(l[i]) <=0:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
            j+=1
    return l[j:]

def findMissing(l):
    l=segregate(l)
    size=len(l)
    for i in range(size):
        x=abs(int(l[i]))
        print(l)
        if x<=size and int(l[x-i])>0:
            l[x-1]="-"+l[x-1]
    miss=size+1
    print("final",l)
    for i in range(size):
        if int(l[i])>0:
           miss=i+1
           break
    print(l)
    return miss
    

if __name__=="__main__":
    l=[]
    while True:
        a=input("Enter an element: ");
        if a=="":
            break
        l.append(a)
    print(findMissing(l))
    
