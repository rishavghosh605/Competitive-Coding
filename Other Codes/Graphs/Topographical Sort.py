from collections import defaultdict

#My way
def topological_sort():
    
    for vertex in visited_list.keys():
        if visited_list[vertex]==False:
            _topological_sort([vertex])
def _topological_sort(vertices):
    
    for v in vertices:
        if v in adjacency_list.keys():
            _topological_sort(adjacency_list[v])
        if visited_list[v]==False:
            visited_list[v]=True
            output_stack.append(v)
    
    return 
#Their Way
def Topology_Sort(vertex):
    if not visited_list[vertex]:
        visited_list[vertex] = True
        for neighbor in adjacency_list[vertex]:
            Topology_Sort(neighbor)
        output_stack.insert(0, vertex)


if __name__=="__main__":
    #storing edge information in adjacency list
    adjacency_list = defaultdict()
    adjacency_list['a']=['c']
    adjacency_list['b']=['c']
    adjacency_list['c']=['d']
    adjacency_list['d']=['f']
    adjacency_list['e']=['f']
    adjacency_list['f']=['g']
    adjacency_list['g']=[] 

    print(adjacency_list.keys())
    '''
    The graph
    a-->d-->e<--c
        ^
        |
        b
    '''
    #Store visited vertex information in visited_list
    visited_list = defaultdict()
    visited_list['a']=False
    visited_list['b']=False
    visited_list['c']=False
    visited_list['d']=False
    visited_list['e']=False
    visited_list['f']=False
    visited_list['g']=False
    
    output_stack=[]
    topological_sort()
    print("My way: ",output_stack[::-1])
    output_stack=[]
    visited_list['a']=False
    visited_list['b']=False
    visited_list['c']=False
    visited_list['d']=False
    visited_list['e']=False
    visited_list['f']=False
    visited_list['g']=False
    for vertex in visited_list:
        Topology_Sort(vertex)
    print("Their way",output_stack)
    
'''
time complexity:
O(V+E)

space complexity:
2 dictionaries, 1 list required
'''

    
    
