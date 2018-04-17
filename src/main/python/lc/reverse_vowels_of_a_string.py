class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = [c for c in s]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, len(arr) - 1
        while left < right:
            while arr[left] not in vowels and left < right:
                left += 1
            while arr[right] not in vowels and left < right:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1
            else:
                return ''.join(arr)
        return ''.join(arr)
