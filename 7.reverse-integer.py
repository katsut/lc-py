#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        min_i32 = 2 ** 31 * -1
        max_i32 = min_i32 * -1 + 1
        reversed = int(bin(x)[0]+str(abs(x))[::-1])
        print(reversed, min_i32, max_i32)
        return reversed if reversed in range(min_i32, max_i32) else 0
# @lc code=end

