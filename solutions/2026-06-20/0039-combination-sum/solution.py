# Number: 0039
# Title: Combination Sum
# Difficulty: Medium
# Tags: Array, Backtracking
# Language: Python3
# URL: https://leetcode.com/problems/combination-sum/
# Date: 2026-06-20
# Runtime: 0 ms (Beats 100%)
# Memory: N/A

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        if len(candidates) == 0:
            return []
        def dfs(i, cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0, [], 0)
        return res