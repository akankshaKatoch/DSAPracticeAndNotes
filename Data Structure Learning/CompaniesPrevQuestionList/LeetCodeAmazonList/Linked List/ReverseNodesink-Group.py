from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()

        dummy.next = head
        prev_group  = dummy 

        def length(node):
            count = 0
            while node:
                count += 1
                node = node.next

            return count     

        len = length(head)

        while len >= k:

            curr = prev_group.next
            nextgroup = curr

            #This will give you the next group element
            for i in range(k):
                nextgroup = nextgroup.next 

            #reverse the curr node group.

            prev = None
            node = curr
            for i in range(k):
                temp = node.next
                node.next = prev
                prev = node
                node = temp

            prev_group.next = prev
            curr.next = nextgroup
            prev_group = curr
            len -=k
        
        return dummy.next





        