def quickSort(intervals):
    start=0
    end=len(intervals)-1
    _quickSort(start,end,intervals)

def _quickSort(start,end,intervals):

    if start==end:
        return intervals[start]
    if start>end:
        return None
    mid=(start+end)//2
    half1 =_quickSort(start,mid,intervals)
    half2 =_quickSort(mid+1,end,intervals)
    arr = merge(half,half2)
    return arr

def merge(half1,half2):

    i=0
    j=0
    arr=[]
    while i<len(half1) and j<len(half2):

        if half1[i]>half2[j]:
            arr.append(half2[j])
            j+=1
            
        elif half1[i]<half2[j]:
            arr.append(half1[i])
            i+=1

        else:
            
            arr.append(half1[i])
            arr.append(half2[j])
    

    while i<len(half1) or j<len(half2):
        
        if i<len(half1):
            arr.append(half1[i])
            i+=1
        if j<len(half2):
            arr.append(half2[j])
            j+=1
         
            
        
       
    print(arr)

if __name__=="__main__":

    intervals=[(1, 3), (5, 8), (4, 10), (20, 25)]
    #quickSort(intervals)
    #mergeIntervals(intervals)
    merge([1,4,6],[2,3,7])
