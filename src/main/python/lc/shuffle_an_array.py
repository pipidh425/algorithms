class Solution(object): # O(N) space, O(N) time for shuffle, O(1) time for reset

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        self.shuffled = [v for v in nums]
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self): 
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # fisher yates shuffle
        for i in range(len(self.shuffled) - 1):
            rndIdx = random.randint(i, len(self.shuffled) - 1)
            self.shuffled[i], self.shuffled[rndIdx] = self.shuffled[rndIdx], self.shuffled[i]
        return self.shuffled
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
