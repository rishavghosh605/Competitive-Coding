"""
This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological
order,write a function that calculates the maximum profit you could have made
from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

"""
def best_stock_price(l):

    profit=0
    lmin=l[0]
    # Buying  date:
    bday=0
    # Sell date:
    sday=0
    for i in range(1,len(l)):
        if l[i]-lmin > profit:
            profit=l[i]-lmin
            sday=i
        if l[i]<lmin:
            lmin=l[i]
            bday=i
    print("Buy date: ",bday,"Sell date: ",sday)
    return profit
        

if __name__=="__main__":

    l=list(map(int,input("Enter the stock prices in chronological order: ").split(' ')))
    result=best_stock_price(l)
    print(result)
