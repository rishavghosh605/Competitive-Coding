author="himanshu malhotra"
aa,bb=0,0
n,m=map(int,input().split())
a=map(int,input().split())
b=map(int,input().split())
ct=0
for i in xrange(max(a),min(b)+1):
    for j in a:
        if i%j!=0:
            break
    else:
        for k in b:
            if k%i!=0:
                break
        else:
            ct+=1
print ct
    
# Done in python 2 wont work in 3
