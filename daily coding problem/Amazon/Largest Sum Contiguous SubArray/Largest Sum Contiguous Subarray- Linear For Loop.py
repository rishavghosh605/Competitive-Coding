
def find_max_sum(l):
    
    csum=0
    max_sum=0
    for element in l:
        csum=csum+element if csum+element > element  else element
        max_sum=csum if csum>max_sum else max_sum
        #print(max_sum,csum)
    return max_sum

def find_max_sum_faster(l):
    for i in range(1,len(l)):
            l[i] = max(l[i], l[i-1] + l[i])
    #print(l)
    return max(l) if max(l)>=0 else 0

if __name__=="__main__":

    # List of integers
    l=list(map(int,input("Enter the elements: ").split(' ')))
    max_sum=find_max_sum(l)
    print("1)The maximum sum: ",max_sum)
    max_sum=find_max_sum_faster(l)
    print("2)The maximum sum: ",max_sum)
    
    
