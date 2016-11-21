class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if len(g) == 0 or len(s) == 0:
            return 0
        
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        pos_s = 0
        
        satisfied = 0
        
        for pos_g in range(len(g)):
            if g[pos_g] <= s[pos_s]:
                satisfied += 1
                pos_s += 1
            if pos_s == len(s):
                return satisfied
                
        return satisfied
                
