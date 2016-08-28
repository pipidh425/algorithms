class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max = 2147483647
        int_min = -2147483648
        digit_9 = ord('9')
        digit_0 = ord('0')
        
        str = str.strip() # remove whitespace
        if len(str) == 0:
            return 0
            
        res = 0
        sign = 1
        if str[0] == '-' or str[0] == '+': # remove sign
            sign = 1 if str[0] == '+' else -1
            str = str[1:]
            
        for i in range(len(str)):
            digit = ord(str[i])
            if digit < digit_0 or digit > digit_9: # ignore invalid digit afterwards
                break
            cur = digit - digit_0
            if sign == -1 and -res * 10 - cur <= int_min:
                return int_min
            elif sign == 1 and res * 10 + cur >= int_max:
                return int_max
            else:
                res = res * 10 + cur
                
        return sign * res
            
        
            
        
