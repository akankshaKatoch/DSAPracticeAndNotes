# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head.next
        prev = head
        #prevValue = 0
        while curr:
            if curr.value == prev.val:
                #delete the node
                prev.next = curr.next
            prev = curr
            curr = curr.next
        


