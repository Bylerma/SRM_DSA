# Number: 1189
# Title: Maximum Number of Balloons
# Difficulty: Easy
# Tags: Hash Table, String, Counting
# Language: Python3
# URL: https://leetcode.com/problems/maximum-number-of-balloons/
# Date: 2026-06-22
# Runtime: 0ms (Beats 100%)
# Memory: 19.06MB (Beats 100%)

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        b = counts['b']
        a = counts['a']
        l = counts['l'] // 2
        o = counts['o'] // 2
        n = counts['n']
        return min(b, a, l, o, n)