# 1752. Check if Array Is Sorted and Rotated

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Tag: Array](https://img.shields.io/badge/Tag-Array-blue)

## 🔗 Link
[LeetCode Problem URL](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)

## 📝 Problem Description
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 
Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].


Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.


Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.


 
Constraints:


	1 <= nums.length <= 100
	1 <= nums[i] <= 100

## 💡 Approach & Notes
<!-- Describe your approach, notes, and complexity here (e.g., O(n) time, O(1) space) -->

## 📊 Submission Stats
| Language | Runtime | Memory | Date |
| --- | --- | --- | --- |
| Python3 | 20260ms (Beats 100%) | N/A | 2026-06-18 |
