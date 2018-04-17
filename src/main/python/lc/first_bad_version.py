# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        suspicious = -1
        
        while left <= right:
            mid = (left + right) / 2
            if isBadVersion(mid):
                suspicious = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return suspicious
                
        
