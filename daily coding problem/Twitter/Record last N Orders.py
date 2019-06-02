'''
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.

'''

class Logs(object):

    def __init__(self,n):

        self.size=n
        self.logger=[None]*self.size
        self.current_items=0
        
    def record(self,order_id):
        if self.current_items==self.size:
            self.current_items=0
        self.logger[self.current_items]=order_id
        self.current_items+=1

    def get_last(self,i):

         start_index=self.current_items-i
         if start_index>=0:
             return self.logger[start_index:self.current_items]
         else:
             return self.logger[start_index:] + self.logger[:self.current_items]

if __name__=="__main__":
    n=int(input("Enter size of n: "))
    log=Logs(n)
    for order_id in range(20):
        log.record(order_id)

    print(log.get_last(0))
    print(log.get_last(0))
    print(log.get_last(1))
    print(log.get_last(3))
    log.record(20)
    log.record(21)
    print(log.get_last(0))
    print(log.get_last(1))
    print(log.get_last(3))
    
    
'''
[]*2=[]
[None]*2=[None,None]
5 6 3 4
  c s
1 2 3 4 5
    s   c
do not use append() here as when you are trying to use a list as an  array
you neeed to understand the fact that you have a fixed size and thus can enter
only a fixed number of elements unlike in a list so you need to have a counter
called index which helps you know how many elements you have entered

>>> l[3:2]
[]
>>> l[2:3]
[2]

l[-1:]
[9]
>>> l[:-1]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> l[-2:]
[8, 9]
>>> 
'''
