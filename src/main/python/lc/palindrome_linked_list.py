# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.head_pos = None
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if self.head_pos is None:
            self.head_pos = head
        if head is None:
            return True
        if(not self.isPalindrome(head.next)):
            return False
        if (self.head_pos.val != head.val):
            return False
        self.head_pos = self.head_pos.next
        return True
