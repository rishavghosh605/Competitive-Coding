"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""
def findNPerfectNumber2(n):
    
    count=0
    curr=19
    while True:
        sums=0
        x=curr
        
        while x>0:
            sums=sums+x%10
            x=int(x/10)
            
        if (sums == 10): 
            count+= 1;
    
        if count==n:
            return curr
        curr += 9 
        
    return -1; 
def chooseN(n):
    while True:
        sums=list(map(int,list(str(n))))
        if sum(sums)<10:
            return n
        n+=1
def findNPerfectNumber1(n):
    
    nPerfect=10*chooseN(n)
    digit=0
    sums=0
    for i in str(nPerfect):
        sums+=int(i)
    digit=10-sums
    nPerfect+=digit
    return nPerfect
    

if __name__=="__main__":

    n=int(input("Enter n: "))
    print(findNPerfectNumber1(n))#Incorrect
    print(findNPerfectNumber2(n))#Correct
    
