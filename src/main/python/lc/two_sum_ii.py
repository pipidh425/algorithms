class Solution(object):
    # O(nlogn) time, O(1) space
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(numbers) - 1):
            start, end = i + 1, len(numbers) - 1
            diff = target - numbers[i]
            while start <= end:
                mid = (start + end) / 2
                if numbers[mid] == diff:
                    return [i + 1, mid + 1]
                elif numbers[mid] < diff:
                    start = mid + 1
                else:
                    end = mid - 1
                
        return None
