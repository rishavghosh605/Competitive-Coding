import numpy as np

def findIslands(pos,world,count):
    
    count,world=markLand(pos,world,count)

    pos=findLand(pos,world)
    if pos==None:
        return count
    else:
        result=findIslands(pos,world,count)
    return result

def markLand(pos,world,count):
    print("\n\nNextIsland\n")
    from queue import Queue
    q=Queue()
    count+=1
    q.put(pos)

    while q.qsize()!=0:
        land=q.get()
        world[land[0]][land[1]]=count
        neighbors=findNeighbors(land,world)
        for neighbor in neighbors:
            q.put(neighbor)

    print(np.array(world))
    return count,world

def findNeighbors(land,world):
    dr=[-1,1,0]
    dc=[-1,1,0]
    neighbors=[]
    for r in dr:
        for c in dc:
            if (r,c)!=(0,0) and r+land[0]>=0 and r+land[0]<len(world) and c+land[1]>=0 and c+land[1]<len(world[0]):
                
                if world[r+land[0]][c+land[1]]==1:
                    neighbors.append((r+land[0],c+land[1]))
    return neighbors
                
    
def findLand(pos,world):
    for i in range(0,len(world)):
        for j in range(0,len(world[0])):
            if world[i][j]==1:
                
                return (i,j)
    return None

def createWorld(world):
    n=int(input("Enter the number of ones: "))
    for i in range(n):
        r,c=tuple(map(int,input("Enter the coordinates: ").split()))
        world[r][c]=1
    print(np.array(world))
if __name__=="__main__":

    #m=int(input("Enter the columns: "))
    #n=int(input("Enter the rows: "))

    world=[[1, 1, 0, 0, 0], [0, 1, 0, 0,1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]
    #[[0 for i in range(m)] for j in range(n)]

    #createWorld(world)
    start=findLand((0,0),world)
    count=1
    result=findIslands(start,world,count)
    print("Number of islands: ",result-1)
