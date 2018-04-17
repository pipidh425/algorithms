class Solution(object):
    def integerBreak(self, n): # the largest product would be the one multiplied by evenly distributed factors
        """
        :type n: int
        :rtype: int
        """
        largest = 0
        for i in range(2, n + 1): # number of factors
            largest = max(largest, math.pow(n / i + 1, n % i) * math.pow(n / i, i - n % i))
            
        return int(largest)
