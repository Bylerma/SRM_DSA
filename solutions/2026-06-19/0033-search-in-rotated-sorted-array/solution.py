# Number: 0033
# Title: Search in Rotated Sorted Array
# Difficulty: Medium
# Tags: Array, Binary Search
# Language: Python3
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Date: 2026-06-19
# Runtime: N/A
# Memory: N/A

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        
        return low
