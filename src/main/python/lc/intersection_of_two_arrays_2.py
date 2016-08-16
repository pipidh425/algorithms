class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        
        len1, len2 = len(nums1), len(nums2)
        small = nums1 if len1 <= len2 else nums2
        large = nums1 if len1 > len2 else nums2
        
        small_map = defaultdict(int)
        for e in small:
            small_map[e] += 1
            
        res = []
        for e in large:
            if small_map[e] > 0:
                res.append(e)
                small_map[e] -= 1
                
        return res
                
            
