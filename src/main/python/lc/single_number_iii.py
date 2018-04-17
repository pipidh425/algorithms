class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0 # will get xor = a^b
        for num in nums:
            xor ^= num
        mask = 1 # will store the last digit that a is different from b
        while xor & mask == 0:
            mask <<= 1
            
        # the mask would divide nums into 2 groups, a and b would be in different groups,
        # the other numbers will be cancled out
        a, b = 0, 0
        for num in nums:
            if num & mask == 0:
                a ^= num
            else:
                b ^= num
                
        return [a, b]
