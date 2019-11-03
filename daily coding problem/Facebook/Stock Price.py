"""
This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.


"""
"""
Three Cases:
1> Where k=1
2> Where k=2
3> Where k=1..k
"""
def case1(l):
    #lets create a temp list
    temp=[0]*len(l)
    b=l[0]
    for i in range(len(l)):
        temp[i]=l[i]-b
        if temp[i]<0:
            b=l[i]
    print(max(temp),temp)
                
if __name__=="__main__":
    
    l=list(map(int,"100, 180, 260, 310, 40, 535, 695".split(", ")))
    case1(l)
    
#input("Enter the stocks: ")
