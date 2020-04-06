class Line {   
     synchronized public void getLine() { 
    	System.out.println("Train "+ Thread.currentThread().getName()+" is given line");
        for (int i = 0; i < 3; i++){        	
            System.out.println(i); 
            try { 
                Thread.sleep(5000); 
             } 
            catch (Exception e){System.out.println(e);} 
        } 
    } //end of getLine()
}  //end of Line
class Train extends Thread{ 
    // Reference variable of type Line. 
    Line line;   
    Train(Line line,String s)
    { 
        super(s);
    	this.line = line; 
    } 
      public void run()    {    	  
        line.getLine(); 
    } 
}   
public class synchronizeds { 
    public static void main(String[] args)    { 
        Line obj = new Line();   
        // we are creating two threads which share 
        // same Object. 
        Train train1 = new Train(obj,"One"); 
        Train train2 = new Train(obj,"Two");   
        // both threads start executing . 
        train1.start(); 
        train2.start(); 
    } 
} 
