class Solution(object):
    # O(1) space and O(1) time as the number of combination is constant 12 * 59
    def dfs(self, n, hours, mins, idx, res):
        if hours >= 12 or mins > 59:
            return
        if n == 0:
            res.append(str(hours) + ":" + "0" * (mins < 10) + str(mins))
        else:
            for i in range(idx, 10):
                if i < 4:
                    self.dfs(n - 1, hours | (1 << i), mins, i + 1, res)
                else:
                    self.dfs(n - 1, hours, mins | (1 << (i - 4)), i + 1, res)
        
    
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        self.dfs(num, 0, 0, 0, res)
        return res
        
