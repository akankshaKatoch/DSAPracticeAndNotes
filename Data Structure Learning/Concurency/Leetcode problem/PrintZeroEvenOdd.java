import java.util.concurrent.*;
import java.util.function.IntConsumer;

class ZeroEvenOdd{

    private int n;
    private Semaphore semaZero = new Semaphore(1);
    private Semaphore semaOdd = new Semaphore(0);
    private Semaphore semaEven = new Semaphore(0);
    private int current = 1;

    public ZeroEvenOdd(int n){
        this.n = n;
    }
    public void zero(IntConsumer printNumber) throws InterruptedException{
        for(int i = 1; i<=n; i++){
            semaZero.acquire();
            printNumber.accept(0);
            if (i % 2 == 0){
                semaEven.release();
            } else{
                semaOdd.release();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException{


    }

    public void odd(IntConsumer printNumber) throws InterruptedException{

        
    }


}


public class PrintZeroEvenOdd {

    public static void main(String[] args) {

        Runnable printNumber = () -> System.out.println(7);
        
    }
    
}
