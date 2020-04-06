class MakeColdCoffee{      
    public synchronized void accessMilk(){
    	try{
        System.out.println("Milk Accessed by "+Thread.currentThread().getName());
        System.out.println("Now... "+Thread.currentThread().getName()+" will take 5 seconds to get milk...");
        Thread.sleep(5000);
        System.out.println(Thread.currentThread().getName()+" now trying to access Coffee Powder");
    	}// end of try
    	catch(InterruptedException e){}
        }// end of accessMilk
    public synchronized void accessCoffeePowder(){
    	try{
        System.out.println(Thread.currentThread().getName()+" accessing Coffee Powder");
        Thread.sleep(5000);
    	}
    	catch(InterruptedException e){}
    }//end of accessCoffeePowder
} // end of MakeColdCoffee

class TH1 extends Thread{
	MakeColdCoffee obj;	
	TH1(String s,MakeColdCoffee coff)	{
		super(s);
		obj=coff;
	}
	public void run()	{
		obj.accessMilk();
		obj.accessCoffeePowder();
		System.out.println(Thread.currentThread().getName()+" made the coffee");
	}
}
class TH2 extends Thread{
	MakeColdCoffee obj;	
	TH2(String s,MakeColdCoffee coff)	{
		super(s);
		obj=coff;
	}
	public void run()	{
		obj.accessMilk();
		obj.accessCoffeePowder();
		System.out.println(Thread.currentThread().getName()+" made the coffee");
	}
}
public class synchronized2{
	public static void main(String[] args){
		MakeColdCoffee Coffee=new MakeColdCoffee();
		TH1 t1= new TH1("Jhon",Coffee);
		TH2 t2= new TH2("Kenny",Coffee);
		t1.start();
	    t2.start();
	}
}
