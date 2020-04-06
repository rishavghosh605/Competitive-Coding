import java.util.*;  
class Student implements Comparable<Student>{  
int rollno;  
String name;  
int age;  
Student(int rollno,String name,int age){  
this.rollno=rollno;  
this.name=name;  
this.age=age;  
}  
@Override
public int compareTo(Student st){  
if(age==st.age)  
return 0;  
else if(age>st.age)  
return 1;  
else  
return -1;  
}  
}  
//Creating a test class to sort the elements  
public class comparable_demo{  
public static void main(String args[]){  
ArrayList<Student> al=new ArrayList<>();  
al.add(new Student(101,"Vijay",23));  
al.add(new Student(106,"Ajay",27));  
al.add(new Student(105,"Jay",21));  
  
Collections.sort(al,Comparator.reverseOrder());  
al.forEach((st) -> 
   {System.out.println(st.rollno+" "+st.name+" "+st.age);}
   );  
}  
}  
