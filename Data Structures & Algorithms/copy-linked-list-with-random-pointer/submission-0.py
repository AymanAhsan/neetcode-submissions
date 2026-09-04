"""
import copy
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        list_map = { None : None}
        curr = head
        while curr:
            copy_node = Node(curr.val)
            list_map[curr] = copy_node
            curr = curr.next
        curr = head
        while curr:
            copy = list_map[curr]
            copy.next = list_map[curr.next]
            copy.random = list_map[curr.random]
            curr = curr.next
        return list_map[head]


