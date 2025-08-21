import java.util.concurrent.Semaphore;

public class Printorder {
    private Semaphore semaSec = new Semaphore(0);
    private Semaphore semaThird = new Semaphore(0);

    public Printorder(){}

    public void first(Runnable printFirst) throws InterruptedException{
        printFirst.run(); 
        semaSec.release();
    }

    public void second(Runnable printSecond) throws InterruptedException{
        semaSec.acquire();
        printSecond.run();
        semaSec.release();
    }

    public void third(Runnable printThird) throws InterruptedException{
        semaThird.acquire();
        printThird.run();
    
    }
    
}
