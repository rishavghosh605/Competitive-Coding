"""
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned
into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
it would return true, since we can split it up into {15, 5, 10, 15, 10}
and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.
"""
def if_Partitioned(arr):
    index=0
    if sum(arr)%2==1:
        print("Cannot be partitioned")
    # The sum we need to search for:
    s=sum(arr)//2
    print(find_partitions1([],[],arr,s,index))
    print("2",find_partitions2([],arr,s,index))

def find_partitions2(s1,arr,s,index):
    print("s1: ",s1)
    
    if index==len(arr):
        
        if sum(s1)==s :
            print("The partitioned sets:",s1," and sum is",s)
            return True        
        return False
    
    if(find_partitions2(s1+[arr[index]],arr,s,index+1)):
          return True
    if(find_partitions2(s1,arr,s,index+1)):
          return True

    return False
def find_partitions1(s1,s2,arr,s,index):
    print("s1: ",s1)
    print("s2: ",s2)
    
    if index==len(arr):
        
        if sum(s1)==s and sum(s2)==s:
            print("The partitioned sets:",s1,s2," and sum is",s)
            return True        
        return False
    
    if(find_partitions1(s1+[arr[index]],s2,arr,s,index+1)):
          return True
    if(find_partitions1(s1,s2+[arr[index]],arr,s,index+1)):
          return True

    return False


if __name__=="__main__":

    # arr stores the multiset
    arr=list(map(int,input("Enter the list of integers: ").split(' ')))

    # To check if the list can be partitioned or not
    if_Partitioned(arr)
    
    
