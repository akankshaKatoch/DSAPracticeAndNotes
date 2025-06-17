from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # This is needed so ListNode can be compared in heapq
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Step 1: Add the first node of each list to heap
        for l in lists:
            if l:
                heapq.heappush(min_heap, l)

        dummy = ListNode(0)
        curr = dummy

        # Step 2: Extract the min and push next node from the same list
        while min_heap:
            node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, node.next)

        return dummy.next








lists = [[1,4,5],[1,3,4],[2,6]]
sol = Solution()
print(sol.mergeKLists(lists))
        