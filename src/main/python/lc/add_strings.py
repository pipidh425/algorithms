class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        max_len = max(len1, len2)
        carry = 0
        res_str = ''
        for i in range(0, max_len):
            loc1, loc2 = len1 - i - 1, len2 - i - 1
            v1 = ord(num1[loc1]) - ord('0') if loc1 >= 0 else 0
            v2 = ord(num2[loc2]) - ord('0') if loc2 >= 0 else 0
            if v1 + v2 + carry >= 10:
                res_str += str(v1 + v2 + carry - 10)
                carry = 1
            else:
                res_str += str(v1 + v2 + carry)
                carry = 0
            
        if carry == 1:
            res_str += '1'
            
        return res_str[::-1]
