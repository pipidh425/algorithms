# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
            
        pre = None
        cur = head
        next = head.next
        
        while cur is not None:
            cur.next = pre
            pre = cur
            cur = next
            if next is not None:
                next = next.next
            
        return pre
