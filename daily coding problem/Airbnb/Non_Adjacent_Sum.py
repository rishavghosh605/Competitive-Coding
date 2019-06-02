
def helper(l,k):
    if k<=0:
        return 0
    if k==1:
        return l[len(l)-k]
    result1=l[len(l)-k]+helper(l,k-2)
    if k>2:
        result2=l[len(l)-k+1]+helper(l,k-3)
        return result1 if result1>result2 else result1
    return result1
def largest_sum(l):
    return helper(l,len(l))
def get_list(n):
    l=n.split(' ')
    return list(map(int,l))

if __name__=="__main__":
    n=input("Enter spaced integers: ")
    l=get_list(n)
    result=largest_sum(l)
    print(result)
    
