'''Good morning! Here's your coding interview problem for today.

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''
'''
def findPair(n,space):
    a=int(n[0:space])
    b=int(n[space+1:])
    t=cons(a,b)
    print(car(cons(a,b)))
    print(cdr(cons(a,b)))

def cons(a, b):
    def pair():
        return (a, b)
    return pair

def car(t):
    return(t()[0])

def cdr(t):
    return(t()[1])
if __name__=='__main__':
    n=input('Enter the pair of integers')
    try:
        space=n.index(" ")
    except Exception as e:
        space=None
        
    if(space!=None):
        findPair(n,space)
    else:
        print("Two integers were not entered")

'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    
    def left(a,b):
        return a
    print("f",f)
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)

print(car(cons(3,4)))
print(cdr(cons(3,4)))
# Other solutions:
# https://galaiko.rocks/posts/2018-07-06/
# https://stackoverflow.com/questions/52481607/dont-understand-the-inner-function-in-python
