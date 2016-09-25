class Solution(object):
    def findNthDigit(self, n):
        start, digits_in_num, nums_in_range = 1, 1, 9
        while n > digits_in_num * nums_in_range:
            n = n - (digits_in_num * nums_in_range)
            digits_in_num += 1
            nums_in_range *= 10
            start *= 10
        return int(str(start + (n - 1) // digits_in_num)[(n - 1) % digits_in_num])























