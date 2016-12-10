class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        prev_is_space = True
        for c in s:
            if c == ' ':  # current is character
                if prev_is_space is False:
                    count += 1
                prev_is_space = True
            else:
                prev_is_space = False

        if prev_is_space is False:
            count += 1
            
        return count
