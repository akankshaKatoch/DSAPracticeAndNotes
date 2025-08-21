from threading import Semaphore

class Printorder:
    def __init__(self):
        self.second_ready = Semaphore(0)
        self.third_ready = Semaphore(0)
    
    def first(self, printFirst):
        printFirst()
        self.second_ready.release()
    
    def second(self, printSecond):
        self.second_ready.acquire()
        printSecond()
        self.third_ready.release()

    def third(self, printThird):
        self.third_ready.acquire()
        printThird()
        self.third_ready.release()