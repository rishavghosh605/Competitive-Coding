class MyGen<T>{  
    T data;  
    void add(T d){this.data=d;}  
    T get(){return data;}  
    }  
public class simple {
    public static void main(String ar[])
    {
        MyGen<Integer> m=new MyGen<>();  
        m.add(2);  
        //m.add("vit");//Compile time error  
        System.out.println(m.get());  
}}
