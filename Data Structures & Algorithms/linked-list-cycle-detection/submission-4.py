# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        index = 0
        seen = {}
        curr = head
        
        while curr:
            if curr in seen:
                return True
            seen[curr] = index
            curr = curr.next
            index += 1
        return False