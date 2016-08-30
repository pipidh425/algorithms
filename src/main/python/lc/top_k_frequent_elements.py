class Solution(object):
    def topKFrequent(self, nums, k): # O(N) space, O(NlogN) time
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        index = {}
        for i in nums:
            if i not in index:
                index[i] = 1
            else:
                index[i] += 1
                
        sorted_pair = sorted([(key, val) for key, val in index.iteritems()], key = lambda t: -t[1])
                
        return [p[0] for p in sorted_pair[:k]]
        
