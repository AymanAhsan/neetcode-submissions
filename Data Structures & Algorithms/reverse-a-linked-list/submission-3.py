# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedArr = []
        current = head
        while current:
            reversedArr.insert(0, current.val)
            current = current.next
        
        # Handle empty list
        if not reversedArr:
            return None

        # Create head node
        new_head = ListNode(reversedArr[0])
        current = new_head

        # Create remaining nodes
        for i in range(1, len(reversedArr)):
            current.next = ListNode(reversedArr[i])
            current = current.next

        return new_head
        
        

            
