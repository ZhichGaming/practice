# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

'''
# This solution doesn't work because c.val is not unique.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        c = head

        while c is not None:
            if c.val in visited:
                return True

            visited.add(c.val)
            c = c.next
        
        return False
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Works but could be optimized. No need for checking slow is None, check fast and fast.next is None.
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next

            if fast is None: # Pointless if use the approach in last comment
                return False
            
            fast = fast.next

            if slow is fast:
                return True
            
        return False
        
