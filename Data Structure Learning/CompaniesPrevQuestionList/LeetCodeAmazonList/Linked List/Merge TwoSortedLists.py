from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """val from list 1 and val from list 2
        if val from ist 1 is less than va from ist 2 appent to the list
            1      2 ---> 4 ---> None
            |    / |
            v   / 
            1      3 ---> 4 ---> None"""

        if not list1:
            return list2
        if not list2:
            return list1
        
        dummyNode = ListNode()
        curr = dummyNode
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        
        curr.next = curr1 if curr1 else curr2

        return dummyNode.next



            




        





list1 = [1,2,4]
list2 = [1,3,4]
#Output: [1,1,2,3,4,4]