# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        
        dummy.next = head.next
        prev = dummy 

        while prev.next and prev.next.next:
            #first node and seconf node we need to swap
            first = prev.next
            second = prev.next.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first 

        return dummy.next 
            
            





        