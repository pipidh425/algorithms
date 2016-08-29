class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        map_s = {}
        for c in s:
            if c not in map_s:
                map_s[c] = 1
            else:
                map_s[c] += 1
                
        for c in t:
            if c not in map_s or map_s[c] == 0:
                return str(c)
            else:
                map_s[c] -= 1
                
        return None
