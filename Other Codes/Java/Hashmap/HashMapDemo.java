//HashMap implements Map interface (key,value) pair
import java.util.*;
public class HashMapDemo{
    public static void main(String[] args){
        HashMap<Integer,String> hmap = new HashMap<Integer,String>();//Considering key as integer and object as string
        hmap.put(1,"one");//We put values in hashmap by using the put method with the arguments key,value
        hmap.put(2,"two");
        hmap.put(3,"three");
        hmap.put(4,"four");
        hmap.put(5,"five");
        System.out.println("Size of the hashMap: "+hmap.size());
        System.out.println(hmap.get(2));//Usinfg get method we can use key to get corresponding value
        //To display all key value pairs
        for(Map.Entry<Integer,String> entry: hmap.entrySet())
        {
            int key = entry.getKey();
            String value = entry.getValue();
            System.out.println(key+" : "+value); 
        }
    }
}