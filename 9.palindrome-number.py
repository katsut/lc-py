#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        h = int(len(s)/2)
        return s[:h] == s[:h*-1-1:-1]


# @lc code=end

