What is multi Threading?

Multi threading is ability of a CPU to execute multiple threads concurrently. 

- A thread is a light weight sub process. 
- In Java, each thread runs a piece of code independently. 
- You create thes threads using either

1.) Thread class
2.) Runnable interface
3.) ExecutorService

The problem with multithreading or concurrency are:

WHen multiple threads access and modify shared data it leads to issues like:

- Race conditions: two threads read/write to the same variable at the same time. 
- Inconsistent state: operations dont complete in the intended order. 
- Deadlocks: Thread will wait forever because they are blocked by each other. 

To help us with all these issue syncronisation comes in picture. 

In core java SYncronization keyword is used to lock the access to a block of code or method. 

synchronized(this) {
    // only one thread can enter this block at a time
}

2.) Semaphores

they control the no of threads that can access a resource. 

Semaphore s = new Semaphore(2); // Only 2 threads allowed at once
s.acquire();  // take permit
// critical section
s.release();  // release permit


3.) CyclicBarrier
Used to make a set of threads wait until all reach a barrier point. 

CyclicBarrier barrier = new CyclicBarrier(3);
barrier.await(); // waits for 3 threads to call await()

4.) CountDownLatch
Blocks threads until the latch count reaches Zero. 

CountDownLatch latch = new CountDownLatch(3);
latch.countDown(); // called by each thread
latch.await();   

 ReentrantLock and Condition
More flexible than synchronized, allows waiting and notifying specific conditions.

5. General Strategy for Solving Concurrency Problems
Understand thread limits
(e.g., only 2 H, 1 O at a time for H₂O)

Block extra threads using Semaphore or Lock

Wait for other threads to reach a point using CyclicBarrier or CountDownLatch

Run Runnable only when conditions are satisfied

Release control/permit after completing
