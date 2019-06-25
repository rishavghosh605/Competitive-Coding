"""
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""
count=[0]
def find_subset(l,k):
    index=0
    sum_till_now=0
    stop=[0]
    S=find_subset_of_sum(l,k,sum_till_now,index,stop)
    return S

def find_subset_of_sum(l,k,sum_till_now,index,stop):
    count[0]+=1
    if stop[0]==1:
        return None
    if sum_till_now ==k:
        stop[0]=1
        return []
    if index == len(l):
        return None
    
    include=None
    sum_till_now+=l[index]
    if sum_till_now <= k:
        include=find_subset_of_sum(l,k,sum_till_now,index+1,stop)
    exclude=find_subset_of_sum(l,k,sum_till_now-l[index],index+1,stop)
    
    
    if not include == None :
        include.append(l[index])
        return include
    if not exclude == None:
       return exclude
    return None
    

if __name__=="__main__":

    l=list(map(int,input("Enter the list of integers: ").split(' ')))
    k=int(input("Enter the target number k: "))

    S=find_subset(l,k)
    print("The required subset is: ",S[::-1])
    print(count)
