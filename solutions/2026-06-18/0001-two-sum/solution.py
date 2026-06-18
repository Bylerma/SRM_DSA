# Number: 0001
# Title: Two Sum
# Difficulty: Easy
# Tags: Array, Hash Table
# Language: Python3
# URL: https://leetcode.com/problems/two-sum/
# Date: 2026-06-18
# Runtime: 3ms (Beats 100%)
# Memory: N/A

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        