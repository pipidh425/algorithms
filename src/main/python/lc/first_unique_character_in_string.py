class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {}
        uniq_list = []
        min_index = len(s)
        for i in range(len(s)):
            if s[i] not in index:
                index[s[i]] = i
            else:
                index[s[i]] = -1
                
        for k, v in index.items():
            if v != -1:
                min_index = min_index if min_index <= v else v
                
        return -1 if min_index == len(s) else min_index
                
        
