class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        res = 10
        for digit in range(1, n): # count number of unique digit in each range [0, 9], [10, 99), [100, 999], ...
            subtotal = 9
            for j in range(digit): # number of choices in each digit in a number 9 * 9 * 8 * 7 * ...
                subtotal *= (9 - j)
            res += subtotal
            
        return res
