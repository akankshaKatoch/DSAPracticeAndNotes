class MyQueue:

    def __init__(self):
        self.stackin = []
        self.stackout = []
    
    def move(self):
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())

    def push(self, x: int) -> None:
        self.stackin.append(x)
        

    def pop(self) -> int:
        self.move()
        return self.stackout.pop()
        

    def peek(self) -> int:
        self.move()
        return self.stackout[-1]

        

    def empty(self) -> bool:
        return not self.stackin and not self.stackout
        
