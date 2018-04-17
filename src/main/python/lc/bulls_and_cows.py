class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B = 0, 0
        nums = collections.defaultdict(int)
        # calculate A and build index
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                A += 1
            nums[secret[i]] += 1
            
        # calculate A + B
        for e in guess:
            if nums[e] > 0:
                B += 1
                nums[e] -= 1
                
        return '%dA%dB' % (A, B - A)
                
        
