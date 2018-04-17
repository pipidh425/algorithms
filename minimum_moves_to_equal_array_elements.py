class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # increase everything expect one each time to make all number eqaul is 
        # equivalent to decrease one element each time to make all number equal.
        # as each step decrease 1 from the sum, we can see how many steps are 
        # needed to make all elements equal to the min
        return sum(nums) - min(nums) * len(nums)
