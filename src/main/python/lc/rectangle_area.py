class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        
        overlap_height = max(0, min(D, H) - max(B, F))
        overlap_width = max(0, min(C, G) - max(A, E))
        
        return area1 + area2 - overlap_height * overlap_width
