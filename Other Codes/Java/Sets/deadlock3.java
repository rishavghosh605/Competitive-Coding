class Text {
    private String packet;     
    public synchronized void set(String s) {
            try { 
                wait();
            } 
           catch (Exception e){System.out.println(e);}        
        packet=s;
        notify();
    }  //end of set
    public synchronized String get() {
            try {
            	wait();                
              }
            catch (Exception e){System.out.println(e);}      
        notify();
        return packet;
    }//end of get
}//end of Text
class vit1 implements Runnable {
    private Text data; 
    int i;
    vit1(Text d)    {
    	data=d;
    }
    public void run() {
        String packets[]={"I packet","II packet","III packet","IV packet","End"};  
        System.out.println("Start sending the data....");
        for (i=0;i<5;i++)
        {
        	try {
                Thread.sleep(1000);
            } 
            catch (Exception e){System.out.println(e);}
            data.set(packets[i]); 
        }
        System.out.println("End of Sending...."); 
    }
}
class vit2 implements Runnable {
    private Text load;  
    vit2(Text l){
    	load=l;
    }
    public void run() {
    	int i;
    	System.out.println("Start receiving the data....");
    	String receivedMessage = load.get();
        for (i=0;i<4;i++)
        {             
            System.out.println(receivedMessage);
            try {
                Thread.sleep(1000);
            } 
            catch (Exception e){System.out.println(e);}
            receivedMessage = load.get();
            }
        System.out.println("End of Receiving the data");
    }
}
public class deadlock3 {
	public static void main(String[] args) {
	    Text data = new Text();
	    Thread sender = new Thread(new vit1(data));
	    Thread receiver = new Thread(new vit2(data));	     
	    sender.start();
	    receiver.start();
	}
}