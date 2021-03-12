#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = []
        for r in zip(*strs):
            if len(set(r)) > 1:
                break;
            p.append(r[0])
        return ''.join(p)

# @lc code=end

