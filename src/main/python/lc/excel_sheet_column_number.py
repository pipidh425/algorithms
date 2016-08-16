class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda a, b: a * 26 + ord(b) - ord('A') + 1, s, 0)
