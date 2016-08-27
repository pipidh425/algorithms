# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        fake_head = ListNode(-1)
        fake_head.next = head
        
        cur = fake_head
        while cur is not None:
            next = cur.next
            while next is not None and next.val == val:
                next = next.next
            cur.next = next
            cur = next
                
        return fake_head.next
