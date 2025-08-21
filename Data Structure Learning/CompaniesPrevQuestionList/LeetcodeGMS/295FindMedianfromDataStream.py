import bisect
import heapq
class MedianFinder:

    # i liked previous approch better but lets solve using heap 
    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.high)>len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))
    
    def findMedian(self) -> float:
        if len(self.low)>len(self.high):
            return -self.low[0]
        return (-self.low[0]+self.high[0])/2.0


    """
    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        # sorting is missing. 
        bisect.insort(self.arr, num)
        #self.arr.append(num)

    def findMedian(self) -> float:
        n = len(self.arr)
        mid = n//2

        if n%2==1:
            return float(self.arr[mid])
        else:
            
            return (self.arr[mid-1]+self.arr[mid])/2.0

    """       


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()