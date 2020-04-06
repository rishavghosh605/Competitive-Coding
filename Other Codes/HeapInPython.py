import heapq

#intializing heap
li=[5,7,9,1,3]

#using heapify to convert list into heap
heapq.heapify(li)

#printing created heap
print("The created heap is: ",end="")
print(list(li))

#using heappush() to push elements into heap
#pushing 4
heapq.heappush(li,4)

#printing modified heap
print("The modified heap after push is: ",end="")
print(list(li))

#using heappop() to pop smallest element
print("The popped-smallest element is: ",end="")
print(heapq.heappop(li))

#heappushpop and heapreplace functions
li1=[5,7,9,4,3]
li2=[5,9,7,4,3]

#heapifying the lists
heapq.heapify(li1)
heapq.heapify(li2)

#using heappushpop() to push and pop items simultaneously
#pops2
print("The popped item using heappushpop() is: ",end="")
print(heapq.heappushpop(li1,3))
print(li1)
#using heapreplace() to replace elements
print("The popped items using heapreplace() is: ")
print(li2)
print(heapq.heapreplace(li2,6))
print(li2)

#using nlargest and nsmallest functions
li1=[6,47,9,4,3,5,8,10,1]
heapq.heapify(li1)

print("The 3 largest numbers in heap are: ",end="")
print(heapq.nlargest(3,li1))

print("The 3 smallest numbers in heap are: ",end="")
print(heapq.nsmallest(3,li1))
