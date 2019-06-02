import random as r
import math


def estimate_PI(rad,inv,seed):
    r.seed=42
    pi=math.pi
    r2=math.pow(rad,2)
    cp=0
    tp=0
    recordpi=0
    for i in range(inv):
        randx=r.uniform(-rad,rad)
        randy=r.uniform(-rad,rad)
        d2=math.pow(randx,2)+math.pow(randy,2)
        if d2<r2:
            cp+=1
        tp+=1
        newpi=4*(cp/tp)
        if abs(pi-newpi)<abs(pi-recordpi):
            recordpi=newpi
    print(recordpi,seed,abs(pi-recordpi))
    return recordpi
if __name__=="__main__":
    radius=int(input("Enter the radius of the circle: "))
    iterations=int(input("Enter the total iterations: "))
    recordpi=estimate_PI(radius,iterations,100)
    bestseed=100
    for seed in range(100):
        newpi=estimate_PI(radius,iterations,seed)
        if abs(math.pi-newpi)<abs(math.pi-recordpi):
            recordpi=newpi
            bestseed=seed
    print(recordpi,bestseed,abs(math.pi-recordpi))
    
