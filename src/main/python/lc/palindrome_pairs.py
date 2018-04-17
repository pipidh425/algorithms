class Solution(object):
    def is_palindrome(self, word):  # O(l) where l is the string length
        left, right = 0, len(word) - 1
        while left <= right:
            if word[left] != word[right]:
                return False
            left, right = left + 1, right - 1
            
        return True
        
    def palindromePairs(self, words): # O(n * l * l) where n is the number of words and l is the string length
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        word_dict = {}
        for i in range(len(words)):
            word_dict[words[i]] = i
        for i in range(len(words)):
            for pos in range(len(words[i]) + 1):
                prefix = words[i][:pos]
                suffix = words[i][pos:]
                if self.is_palindrome(prefix):  # "b prefix suffix" is a palindrome
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_dict and word_dict[rev_suffix] != i:
                        res.append([word_dict[rev_suffix], i])
                if self.is_palindrome(suffix):  # "prefix suffix b" is a palindrome
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_dict and word_dict[rev_prefix] != i and len(suffix) != 0:
                        res.append([i, word_dict[rev_prefix]])
                    
        return res
        

