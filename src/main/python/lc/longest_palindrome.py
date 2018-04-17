class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = collections.defaultdict(int)
        for c in s:
            index[c] += 1
            
        length = 0
        has_single = False
        for v in index.values():
            if v % 2 == 1:
                has_single = True
            length += v / 2 * 2
            
        return length + (1 if has_single else 0)
