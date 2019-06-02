
def helper(data,k):
    if data=="":
        return 1
    s=len(data)-k
    if data[s]=="0":
        return 0
    result=helper(data[1:],k-1)
    #print("inside helper",result,data[1:],k-1)
    if k>=2 and int(data[s:s+2])<=26:
        result+=helper(data[2:],k-2)
        #print(data,result)
    return result

def num_ways(data):
    return helper(data,len(data))
data=input("enter your data: ")
print("Total no. of ways: ",num_ways(data))
