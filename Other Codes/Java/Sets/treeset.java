import java.util.Iterator;
import java.util.TreeSet;
class sample1{}
public class treeset {
    public static void main(String arg[]){
        TreeSet ts=new TreeSet();
        ts.add("aaa");
        ts.add("ccc");
        ts.add("ddd");
        ts.add("bbb");
        ts.add("SCOPE");
        Iterator it=ts.iterator();
        System.out.println("Elements of TreeSet");
        while(it.hasNext())
            System.out.println(it.next());
           
        /*sample1 s1=new sample1();
        sample1 s2=new sample1();
        TreeSet ts1=new TreeSet();
        ts1.add(s1);
        ts1.add(s2);
        it=ts1.iterator();
        System.out.println("Elements of TreeSet");
        while(it.hasNext())
            System.out.println(it.next());*/
    }
}
