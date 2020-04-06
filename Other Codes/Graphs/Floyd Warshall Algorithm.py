def CreateGraph():
    matrix=[[0,3,float('inf'),7],[8,0,2,float('inf')],[5,float('inf'),0,1],[2,float('inf'),float('inf'),0]]
    return matrix

def FloydWarshall(graph):

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if(k!=i or j!=k):#just optimizing by stopping computation of next line when not required
                    graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

        prettyPrint(graph,k+1)

def prettyPrint(graph,k):
    print("Matrix no.: ",k)
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j],end=" ")
        print()
if __name__=="__main__":

    graph=CreateGraph()
    prettyPrint(graph,0)
    FloydWarshall(graph)
