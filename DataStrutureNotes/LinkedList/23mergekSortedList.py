# Definition for singly-linked list.
from typing import List
from typing import Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list:
            return []
        minheap =[]
        counter = 0
        
        for node in lists:
            if node:
                heapq.heappush(minheap, (node.val, counter, node))
                counter += 1
        print(minheap)
        dummy = ListNode()
        curr = dummy
        while minheap:
            val, count, node = heapq.heappop(minheap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(minheap, (node.next.val, counter, node.next))
                counter += 1
        return dummy.next



# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print("->".join(values) if values else "Empty list")

# Test cases
def test_merge_k_lists():
    solution = Solution()
    
    # Test Case 1: Example from problem statement
    lists1 = [
        create_linked_list([1,4,5]),
        create_linked_list([1,3,4]),
        create_linked_list([2,6])
    ]
    print("Test Case 1:")
    print("Input lists:")
    for lst in lists1:
        print_linked_list(lst)
    merged1 = solution.mergeKLists(lists1)
    print("Merged result:")
    print_linked_list(merged1)
    print()
    
    # Test Case 2: Empty input
    lists2 = []
    print("Test Case 2:")
    print("Input lists: []")
    merged2 = solution.mergeKLists(lists2)
    print("Merged result:")
    print_linked_list(merged2)
    print()
    
    # Test Case 3: Lists with empty lists
    lists3 = [
        create_linked_list([]),
        create_linked_list([1,3,5]),
        create_linked_list([]),
        create_linked_list([2,4,6])
    ]
    print("Test Case 3:")
    print("Input lists:")
    for lst in lists3:
        print_linked_list(lst)
    merged3 = solution.mergeKLists(lists3)
    print("Merged result:")
    print_linked_list(merged3)
    print()
    
    # Test Case 4: Single element lists
    lists4 = [
        create_linked_list([2]),
        create_linked_list([1]),
        create_linked_list([3])
    ]
    print("Test Case 4:")
    print("Input lists:")
    for lst in lists4:
        print_linked_list(lst)
    merged4 = solution.mergeKLists(lists4)
    print("Merged result:")
    print_linked_list(merged4)
    print()
    
    # Test Case 5: Lists with duplicate values
    lists5 = [
        create_linked_list([1,1,2]),
        create_linked_list([1,2,2]),
        create_linked_list([3,3,4])
    ]
    print("Test Case 5:")
    print("Input lists:")
    for lst in lists5:
        print_linked_list(lst)
    merged5 = solution.mergeKLists(lists5)
    print("Merged result:")
    print_linked_list(merged5)

if __name__ == "__main__":
    test_merge_k_lists()