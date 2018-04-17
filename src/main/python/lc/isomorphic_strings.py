class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}
        used = sets.Set()
        
        for i in range(len(s)):
            if s[i] not in map:
                if t[i] not in used: 
                    map[s[i]] = t[i] # map s[i] to t[i]
                    used.add(t[i])
                else: # t[i] has been mapped
                    return False
            elif map[s[i]] != t[i]: # s[i] has been mapped
                    return False
                    
        return True
        
