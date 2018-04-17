class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # This question is equivalent to count number of factor 5 in a sequence,
        # the number of trailing 0 is equivalent to the number of 5.
        # We can find the following patterns:
        # for number < 5^2: 5, 10, 15, 20 each contains one 5 as factor
        # for 5^2 <= number < 5^3: 25, 30, 35, ..., 110, 115, 120, each contains two 5 as factor
        # for 5^n <= number < 5^{n + 1}, each number with multiplier of 5 contains n 5 as factor
        sum, power = 0, 5
        while power <= n:
            sum += n / power
            n /= 5
        return sum
