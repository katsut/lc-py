#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, v1 in enumerate(nums):
            for i2, v2 in enumerate(nums[i1+1:]):
                if v1+v2 == target:
                    return [i1,i1+i2+1]
        return None


# @lc code=end

