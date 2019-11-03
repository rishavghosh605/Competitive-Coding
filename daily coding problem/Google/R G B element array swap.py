"""
This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first,
the Gs come second, and the Bs come last.
You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

"""

# Time Complexity: O(3N)~O(N)
def segregateValue(arr):
    # ioR stores the index where the character R if found will be replaced
    ioR = 0
    for i in range(len(arr)):
        if arr[i]=='R':
            arr[i]=arr[ioR]
            arr[ioR]="R"
            ioR+=1

    # ioG stores the index where the character G if found will be replaced
    ioG = ioR
    for i in range(len(arr)):
        if arr[i]=='G':
            arr[i]=arr[ioG]
            arr[ioG]="G"
            ioG+=1
            
    # ioB stores the index where the character B if found will be replaced
    '''ioB = ioG
    for i in range(len(arr)):
        if arr[i]=='B':
            arr[i]=arr[ioB]
            arr[ioB]="B"
            ioB+=1'''
'''Adding Constraint:
   No extra space allowed(except O(1) space like variables) and minimize the time complexity.
   P.s: You can only traverse the array once.
'''

def threePartition1(arr):

    i=0
    rCount=0
    bCount=len(arr)-1
    
    while i<=bCount:
        #print(arr,i,len(arr))
        if arr[i]=="R":
            arr[i],arr[rCount]=arr[rCount],"R"
            if rCount==i:
                i+=1     
            rCount+=1

        elif arr[i]=="B":
            arr[i],arr[bCount]=arr[bCount],"B"
            if bCount==i:
                i+=1
            bCount-=1
        elif arr[i]=="G":
            i+=1
        

    print(arr)

def threePartition2(arr):

    i=0
    rCount=0
    bCount=len(arr)-1
    
    while i<=bCount:
        #print(arr,i,len(arr))
        if arr[i]=="R":
            arr[i],arr[rCount]=arr[rCount],"R"
            i+=1     
            rCount+=1

        elif arr[i]=="B":
            arr[i],arr[bCount]=arr[bCount],"B"
            bCount-=1
        elif arr[i]=="G":
            i+=1
        

    print(arr)

if __name__=="__main__":

    #arr=['r','g','b','g','b','g','b','r','r','b','g','r','r','b','b','g','r']
    #arr=list(map(str.upper(x),(lambda x: x for x in arr)))
    #arr=['R','G','B','G','B','G','B','R','R','B','G','R','R','B','B','G','R']
    arr=['G', 'B', 'R', 'R', 'B', 'R', 'G']
    #input("Enter the characters R,G,B: ").split(" ")
    #segregateValue(arr)
    print("Segregated array: ", arr)
    threePartition1(arr)
    threePartition2(arr)



