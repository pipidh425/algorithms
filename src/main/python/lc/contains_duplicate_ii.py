class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        size = len(nums)
        prev_occurrance = {}
        
        for i in range(size):
            if nums[i] not in prev_occurrance:
                prev_occurrance[nums[i]] = i
            else:
                if i - prev_occurrance[nums[i]] <= k:
                    return True
                else:
                    prev_occurrance[nums[i]] = i
                    
        return False
