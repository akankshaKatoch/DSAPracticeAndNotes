# Definition for singly-linked list.
from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        #lists = [[1,4,5],[1,3,4],[2,6]]

        heap = []
        for i, node in enumerate(lists):
            heap.append((node.val, i, node))

        heapq.heapify(heap)

        dummy = ListNode()
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next
            ## this step I am little confused. 
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

            
