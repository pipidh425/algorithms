class Solution(object):
    # F(k) = 0 * B_k[0] + 1 * B_k[1] + ... + (n - 1) * B_k[n - 1]
    # F(k - 1) = 0 * B_{k-1}[0] + 1 * B_{k-1}[1] + ... + (n - 1) * B_{k-1}[n - 1]
    #          = 0 * B_k[1] + 1 * B_k[2] + ... + (n - 2) * B_k[n - 1] + (n - 1) * B_k[0]
    # F(k) - F(k - 1) = B_k[1] + B_k[2] + ... + B_k[n - 1] + (1 - n) * B_k[0]
    #                 = sum(A) - n * B_k[0]
    # F(k) = F(k - 1) + sum(A) - n * B_k[0] 
    #      = F(k - 1) + sum(A) - n * A[len(A) - k]
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum_a, len_a = sum(A), len(A)
        fk = 0
        for i in range(len_a):
            fk += i * A[i]
        max_res = fk
            
        for k in range(1, len_a):
            fk = fk + sum_a - len_a * A[len_a - k]
            max_res = max(max_res, fk)
            
        return max_res
        
