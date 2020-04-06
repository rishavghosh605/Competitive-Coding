public class LinkedList{
    Node head;        
    public void insert(int data)
    {
        Node node = new Node();
        node.data = data;
        node.next = null;
        if (head == null)//Checking if the linked list is empty or not
        {
            head=node;
        }
        else
        {
            Node n=head;
            while(n.next!=null)
            {
                n=n.next;
            }
            n.next=node;
        }
    }
    public void insertAtStart(int data)
    {
        Node node = new Node();
        node.data = data;
        node.next = null;
        if(head==null)
            head = node;
        else
        {
            node.next = head;
            head = node;
        }
    }
    public void insertAt(int index, int data)
    {
        Node node = new Node();
        node.data = data;
        node.next = null;
        if(index == 0)
              insertAtStart(data);
        else{
        Node n = head;
        for(int i=0;i<index;i++)
        {
         n=n.next;   
        }
        node.next = n.next;
        n.next = node;
      }
    }
    public void show()
    {
        Node node = head;
        while(node!=null)
        {
            System.out.println("\n"+node.data);
            node=node.next;
        }
    }
}