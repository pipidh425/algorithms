class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = set()
        next = n
        while True:
            next = self.nextNum(next, nums)
            if next == 1:
                return True
            elif next in nums:
                return False
            nums.add(next)
        
    def nextNum(self, cur, nums):
        next = 0
        while cur > 0:
            digit = cur % 10
            next += digit * digit
            cur /= 10
            
        return next
