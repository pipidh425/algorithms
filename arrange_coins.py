class Solution(object):  # O(n) time
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        complete_row = 0
        i = 1
        while n >= i:
            complete_row += 1
            n -= i
            i += 1
                
        return complete_row
