def find_lcm_gcd(num1, num2,ch): 
    if(num1>num2): 
        num = num1 
        den = num2
    else: 
        num = num2 
        den = num1
    rem = num % den
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den
    gcd = den 
    if(ch==1):
        return gcd
    else:
        lcm = int(int(num1 * num2)/int(gcd))
        return lcm

def getTotalX(a, b):
   lm = a[0]   
   hcf = b[0]

   for i in range(1, len(a)): 
    lm = find_lcm_gcd(lm, a[i],2) 
   for i in range(1,len(b)): 
    hcf = find_lcm_gcd(hcf,b[i],1)
   l=[]
   for i in range(0,(hcf//lm)):
    if (hcf%(lm*(i+1))==0):
        l.append(lm*(i+1))
   return (lm,hcf)

if __name__ == '__main__':

    print("Enter the number of integers in arrays a for lcm and b for gcd respectively:")

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    print("Enter the array for computing lcm")

    a = list(map(int, input().rstrip().split()))

    print("Enter the array for computing gcd/hcf")
    
    b = list(map(int, input().rstrip().split()))

    lcm,hcf = getTotalX(a, b)

    print("lcm: ",lcm,"\n","hcf: ",hcf)

# here it is the same logic except we are using loops instead of recursion
# and mod(%) instead of subtraction(-)
# to get the hcf or gcd
