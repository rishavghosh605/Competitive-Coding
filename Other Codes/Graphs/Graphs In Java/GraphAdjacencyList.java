import java.util.*;
public class GraphAdjacencyList{
    private Map<Integer,ArrayList<Integer>> adjListsMap;
    public GraphAdjacencyList(int vertices)
    {
        //We get an input of the number of vertices and we use that to create an empty graph with those vertices
        adjListsMap = new HashMap<Integer,ArrayList<Integer>>();
        for(int i=0;i<=vertices;i++)
        {
            ArrayList<Integer> neighbors = new ArrayList<Integer>();
            adjListsMap.put(i,neighbors);//For every node there is a list of neighbors
        }
    }
    //To add edge
    public void addEdge(int v,int w){
        //v is the vertice and w is the neighbor
        //v>adjListsMap.size() This checks the case that v is 0,1 or 2 but we are trying to add a vertex 7 then we cannot
        
        if(v>adjListsMap.size() || w > adjListsMap.size())
            return;
        
        (adjListsMap.get(v)).add(w);
        (adjListsMap.get(w)).add(v);//If we addd this condition the graph becomes undirected as w is a neighbor of v and v is also a neighbor of w
    }
    
    public ArrayList<Integer> getNeighbors(int v){
        if( v > adjListsMap.size())
            return null;
        return new ArrayList<Integer>(adjListsMap.get(v));
    }
    
    public static void main(String args[]){
        int count=1,source,dest;//source and dest are the source and destination vertex respectively
        System.out.println("Enter the number of vertices and edges: ");
        Scanner sc=new Scanner(System.in);
        int number_vertices = sc.nextInt();
        int number_edges = sc.nextInt();
        GraphAdjacencyList adjacencyList = new GraphAdjacencyList(number_vertices);
        System.out.println("Enter edges in format <source> <destination>");
        while(count<=number_edges){
            source=sc.nextInt();
            dest = sc.nextInt();
            adjacencyList.addEdge(source,dest);
            count++;
        }
        System.out.println("The given adjacency List for the graph\n");
        for(int i=1;i<=number_vertices;i++)
        {
            System.out.print(i+"-->");
            ArrayList<Integer> edgeList = adjacencyList.getNeighbors(i);
            for(int j=1;;j++)
            {
                if(j!=edgeList.size())
                {
                    //If  not last neighbor
                    System.out.print(edgeList.get(j-1)+"-->");
                }
                else{
                    //If last neighbor
                    System.out.print(edgeList.get(j-1));
                    break;
                }
            }
            System.out.println();
        }
    System.out.println();
    }
    
}