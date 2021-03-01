#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # WIP

        m = set()
        cur = 0
        result = s[cur] if s else ''
        for i, c in enumerate(s):
            substr = s[cur:i+1]
            print(substr)

            if c in m:
                # start new substring
                cur = i # reset cursor
                m = {c} # clear set

            else:
                m.add(c)

                if len(substr) > len(result):
                    result = substr


        print(result)
        return len(result)



# @lc code=end

