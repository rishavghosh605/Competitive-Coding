public class Runner{
    public static void main(String[] args){
        LinkedList list = new LinkedList();
        list.insert(18);
        list.insert(45);
        list.insert(12);
        list.insertAtStart(10);
        list.insertAt(2,2);
        list.insertAt(0,5);
        list.show();
    }
}