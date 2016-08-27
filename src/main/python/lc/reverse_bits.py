class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            res <<= 1
            if n & 0b1 == 1:
                res |= 0b1;
            n >>= 1
        return res
