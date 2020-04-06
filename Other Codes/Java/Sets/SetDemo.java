    import java.util.*;
class SetDemo{
    public static void main(String[] args)
    {
        Set<Integer> values = new HashSet<>();//Set is an interface, which is implemented by the class HashSet
        values.add(87);
        values.add(94);
        values.add(6);
        values.add(34);
        values.add(92);        
        System.out.println("Is 6 added: "+values.add(6));//Wont add duplicate value
        System.out.println("Is 10 added: "+values.add(10));
        for(int i : values){
            //Sequence will not be followed that is set is unordered collection of unique values
            System.out.println(i);
        }
        //On the other hand TreeSet creates an ascending order collection 
        Set<Integer> values2 = new TreeSet<>();//Set is an interface, which is implemented by the class HashSet
        values2.add(87);
        values2.add(94);
        values2.add(6);
        values2.add(34);
        values2.add(92);
        System.out.println("Is 6 added: "+values2.add(6));//Wont add duplicate value
        System.out.println("Is 10 added: "+values2.add(10));
        for(int i : values2){
            //Ascending order will  be followed 
            System.out.println(i);
        }
    }
}