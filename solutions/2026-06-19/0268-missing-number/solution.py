# Number: 0268
# Title: Missing Number
# Difficulty: Easy
# Tags: Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting
# Language: Python3
# URL: https://leetcode.com/problems/missing-number/
# Date: 2026-06-19
# Runtime: 0ms (Beats 98%)
# Memory: N/A

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
