# When the next steps rely on the previous steps

# We first import the queue module
import queue

# We initialize a queue
q = queue.Queue()

# We put items in a queue
q.put(5)

# We dequeue here:
print(q.get())

# Checkin if a queue is empty or not
print(q.empty())

# Enqueuing a bunch of elements
for i in range(5):
    q.put(i)

# Dequeuing a bunch of elements
while not q.empty():
    print(q.get(),end=' ')
