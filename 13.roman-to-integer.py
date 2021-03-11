#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'X': 10,
            'C': 100,
            'V': 5,
            'L': 50,
            'D': 500,
            'M': 1000,
        }
        n = 0
        pre = 0
        for c in s[::-1]:
            v = d[c]
            if pre > v:
                n = n - v
            else:
                n = n + v
            pre = v
        return n

# @lc code=end
