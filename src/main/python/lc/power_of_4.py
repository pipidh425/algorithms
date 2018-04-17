class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if a number is 2^n, then num & num - 1 == 0
        # the number with 2^n consists of 2^{2k} and 2^{2k - 1}
        # if the number is 2^{2k}, then (num - 1) % 0
        return num > 0 && (num & num - 1) == 0 && (num - 1) % 3 == 0
        
