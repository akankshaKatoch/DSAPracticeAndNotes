class StockSpanner:

    def __init__(self):
        self.stack = []       

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


        


# Your StockSpanner object will be instantiated and called as such:
#obj = StockSpanner()
#param_1 = obj.next(price)

stockSpanner = StockSpanner()
stockSpanner.next(100) #return 1
print(stockSpanner.next(80))  #return 1
stockSpanner.next(60)  #return 1
stockSpanner.next(70)  #return 2
stockSpanner.next(60)  #return 1
stockSpanner.next(75)  #return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
print(stockSpanner.next(85))  #return 6