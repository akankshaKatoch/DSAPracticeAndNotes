from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 or l2 or carry :
                 
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum = num1+num2+carry
            if sum>=10:
                carry = 1
                sum = sum%10
            else: carry = 0
            curr.next = ListNode(val=sum)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
            

            



l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]
    