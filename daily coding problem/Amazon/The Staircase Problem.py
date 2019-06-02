'''
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

'''
# This is the first way where we use recursion but we will use
# bottom up dynamic programming as we find a relationship
# that is the fibonacci series num_ways(n)=num_ways(n-1)+num_ways(n-2)
def helper(n,steps):
    if n==0:
        return 1
    ways=0
    for i in steps:
        if n-i>=0:
            ways+=helper(n-i,steps)    
    return ways
    
def num_of_ways(n,steps):
    valid_steps=[]
    for i in steps:
        if n-i >= 0:
            valid_steps.append(i)
    return helper(n,steps)
# Used to find number of ways using dynamic programming:
def num_ways_dp(n,steps):
    if n==0:
        return 1
    total_ways={}
    total_ways[0]=1
    for i in range(1,n+1):
        ways=0
        for j in steps:
            if i-j>=0:
                ways+=total_ways[i-j]
        total_ways[i]=ways
    return total_ways
        
if __name__=="__main__":

    n=int(input("Enter the number of steps: "))
    steps=input("Enter ways in which you can climb: ")
    steps_list=list(map(int,steps.split(' ')))
    result=num_of_ways(n,steps_list)
    print("No. of ways: ",result)
    result=num_ways_dp(n,steps_list)
    print("Version 2, No. of ways: ",result)
    
