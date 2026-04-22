# 136. Single Number
# https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        result = 0

        for n in nums:
            result ^= n

        return result
