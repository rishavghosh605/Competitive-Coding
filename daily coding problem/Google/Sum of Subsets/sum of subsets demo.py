"""
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""

def find_subset(l,k):

    index=0
    sum_till_now=0
    S=find_subset_of_sum(l,k,sum_till_now,index)
    return S

def find_subset_of_sum(l,k,sum_till_now,index):

    S=list()
    if index >= len(l):
        return S
    if sum_till_now + l[index]  >= k:
        print(index)
        print("S",S)
        if sum_till_now + l[index] == k:
            print("SS: ",S,k,sum_till_now,index)
            print(S+[3],S,l[index]))
            return [l[index]]
    

    exclude = list()
    include = list()
    exclude=find_subset_of_sum(l,k,sum_till_now,index+1)
    if sum_till_now+l[index] < k:
        include=find_subset_of_sum(l,k,sum_till_now+l[index],index+1)
    print("I",include,S,k,sum_till_now,index)
    print("E",exclude,S,k,sum_till_now,index)
    
    
    if len(include) > 0 :
        S=include
        print("N1:",S)
        return S.append(l[index])
    if len(exclude) > 0:
        S=exclude
        print("N2:",S)
        return S
    print("N:",S,k,sum_till_now,index,include,exclude)
    return S
    

if __name__=="__main__":

    l=list(map(int,input("Enter the list of integers: ").split(' ')))
    k=int(input("Enter the target number k: "))

    S=find_subset(l,k)
    print("The required subset is: ",S)
