class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
            
        hex_map = '0123456789abcdef'
        res = ''
        for i in xrange(8): # 32-bit, each time compare 4-bit
            digit = num & 0b1111
            res = hex_map[digit] + res
            num = num >> 4
            
        pos = 0
        while pos < len(res) and res[pos] == '0':
            pos += 1
            
        return res[pos:]
