import java.util.Random;
class Buffer {
   private volatile int num;
   private boolean state = false;
   public synchronized void set(int n) {
      try {
         while (state) {
            wait();
         }
      } 
      catch (InterruptedException ix) {
         ix.printStackTrace();
      }
      num = n;
      state = true;
      //Thread.sleep(2000);
      notify();
   }
   public synchronized int get() {
      try {
         while (!state) 
            wait(); 
      } 
      catch (InterruptedException ix) {
         ix.printStackTrace();
      }
      state = false;
      //System.out.println("Item " + num);
      notify();
      return num;
   }}
 class Producer implements Runnable {
   private final Buffer syncBuffer;
   Thread proth;
   private final Random r = new Random();
   public Producer(Buffer b) {
      syncBuffer = b;
      proth = new Thread(this, "Producer");
   }  
   public void run() {
      int i = 0;
      while (i++ < 10) {
         int val = r.nextInt(100);
         syncBuffer.set(val);
         System.out.println("Produced value: " + val);
  }}}
 class Consumer implements Runnable {
   private final Buffer syncBuffer;
   Thread conth;
   public Consumer(Buffer b) {
      syncBuffer = b;
      conth = new Thread(this, "Consumer");
   }   
   public void run() {
      int i = 0;
      while (i++ < 10) 
    	System.out.println("Consumed value: " + syncBuffer.get());
   }}
public class synchronizedthreads {
	public static void main(String[] args) {
	      Buffer buff = new Buffer();
	      Producer p = new Producer(buff);
	      Consumer c = new Consumer(buff);

	      
	      c.conth.start();
	      	      p.proth.start();
	   }
}
