//Helps maintain and use dynamic arrays basically decrease and increase at will
import java.util.ArrayList;
public class DynamicArray{
    public static void main(String[] args)
    {
        int simple_array[] = new int [5];
        ArrayList<Integer> myList = new ArrayList<Integer>(5);//5 is the initial size provided
        myList.add(1);
        myList.add(5);
        myList.add(3);
        myList.add(25);
        //myList.add(93);
        
        for(Integer x: myList)
        {
            System.out.println(x);
        }
        System.out.println("Size of list: "+myList.size());
        myList.remove(2);//Remove element at index 2
        myList.set(0,100);//Set the value of a certain index 1 to 100
        myList.trimToSize();//Trime the size of the array to the given size
        myList.clear();//Clear the entire array
    }
}
 