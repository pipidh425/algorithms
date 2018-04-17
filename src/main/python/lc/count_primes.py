class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        is_prime = [True] * (n - 1)
        is_prime[0] = False
        i = 2
        while True:
            if is_prime[i - 1]: # if not marked off
                j = i * i
                while j < n:
                    is_prime[j - 1] = False # mark off multiplier
                    j += i
            i += 1
            if i * i >= n:
                break
                
        return len([x for x in is_prime if x])
