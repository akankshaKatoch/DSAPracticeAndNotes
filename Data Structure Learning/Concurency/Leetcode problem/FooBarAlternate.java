import java.util.concurrent.Semaphore;

class FooBar{
    private int n;
    private Semaphore foosema = new Semaphore(1);
    private Semaphore barsema = new Semaphore(0);

    public FooBar(int n){
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException{

        for (int i = 0; i<n; i++){
            foosema.acquire();
            printFoo.run();
            barsema.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException{

        for (int i = 0; i<n; i++){
            barsema.acquire();
            printBar.run();
            foosema.release();
        }
    }
}

public class FooBarAlternate{
    public static void main(String[] args) {
        FooBar fooBar = new FooBar(5);

        Runnable printFoo = () -> System.out.println("foo");
        Runnable printBar = () -> System.out.println("Bar");

        Thread thread1 = new Thread(()->{
            try {
                fooBar.foo(printFoo);
            } catch (InterruptedException e){
                Thread.currentThread().interrupt();
            }
        });

        Thread thread2 = new Thread(() -> {
            try {
                fooBar.bar(printBar);
            } catch (InterruptedException e){
                Thread.currentThread().interrupt();
            }
        });

        thread1.start();
        thread2.start();
    }
}