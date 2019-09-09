def first(arr,start,end,element):

    mid=(start+end)//2
    if arr[mid]==element and (mid==0 or arr[mid-1]<element):
        print("First Occurrence: ",mid)
    
    elif arr[mid]>element:
        start=mid+1
        first(arr,start,end,element)

    else:
        end=mid-1
        first(arr,start,end,element)

    

def last(arr,start,end,element):

    mid=(start+end)//2
    
    if arr[mid]==element and (mid==len(arr)-1 or arr[mid+1]>element):
        print( "Last Occurrence: ",mid)
    
    elif arr[mid]<element:
        end=mid-1
        last(arr,start,end,element)
        

    else:
        start=mid+1
        last(arr,start,end,element)

if __name__=="__main__":

    arr=list(map(int,input("Enter the sorted array: ").split(' ')))
    start=0
    end=len(arr)
    element=int(input("Enter the element: "))
    first(arr,start,end,element)
    last(arr,start,end,element)
