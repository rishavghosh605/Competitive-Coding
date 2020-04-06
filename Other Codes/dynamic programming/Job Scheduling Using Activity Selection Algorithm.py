def notOverlap(startTime,endTime,i,j):
    if endTime[j] <= startTime[i]:
        return True
    return False

def sortJobs(startTime,endTime,profit,n):

    for i in range(n):
        for j in range(n):
            print(i,j,endTime[i],endTime[j])
            if endTime[i]<endTime[j]:
                temp1=startTime[j]
                startTime[j]=startTime[i]
                startTime[i]=temp1
                temp2=endTime[j]
                endTime[j]=endTime[i]
                endTime[i]=temp2
                temp3=profit[j]
                profit[j]=profit[i]
                profit[i]=temp3
            print(endTime)
    print(profit)
    return (startTime,endTime,profit)
    
def findMaxProfit(startTime,endTime,profit,n):

    startTime,endTime,profit=sortJobs(startTime,endTime,profit,n)
    for i in range(n):
        for j in range(i):
            #print("First Interval: ( ",startTime[i],"-",endTime[i],profit[i]," ) Second interval: ( ",startTime[j],"-",endTime[j],profit[j]," )")
            if(notOverlap(startTime,endTime,i,j)):
                #print("Not Overlapping")
                if profit[i]+profit[j]>profit[i]:
                    profit[i]+=profit[j]

    print(profit)
    return max(profit)

if __name__=="__main__":
    startTime=list(map(int,input("Enter all the start times: ").split()))
    endTime=list(map(int,input("Enter all the end times: ").split()))
    profit=list(map(int,input("Enter all the profits: ").split()))
    n=len(startTime)
    maxProfit = findMaxProfit(startTime,endTime,profit,n)
    print("Max Profit: ",maxProfit)
    
