class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        elif n % 2 == 0:
            return 1 + self.integerReplacement(n >> 1)
        elif (n + 1) % 4 == 0:
            return 1 + self.integerReplacement(n + 1)
        else:
            return 1 + self.integerReplacement(n - 1)
