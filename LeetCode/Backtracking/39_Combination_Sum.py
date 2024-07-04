'''
Problem Link : https://leetcode.com/problems/combination-sum/description/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
'''
# Method 1 - Involves Sorting

class Solution:
    def backtrack(self, n, candidates, res, cur_comb, idx, target, cur_sum):
        # Base Case: If Current Combination's Sum is equals to Target,, then we got a suitable Combination
        if cur_sum == target:
            res.append(cur_comb.copy()) # Shallow Copy,, Other Syntax res.append(cur_comb[::])
            return
        # Also,, There will be some cases where sum(cur_comb) > target,,those Combos are unnecessary
        if cur_sum > target:
            return

        for i in range(idx, n):
            # If Current_Ele is bigger than target,, 
            # then remaining other Ele's which are present at the right side will also be greater than the target,, 
            # so there is no need to check(Benefit of Sorting)

            if candidates[i] > target:
                return

            # "i" is Current Index which we are at,,
            # So take the ith Guy
            cur_comb.append( candidates[i] )
            cur_sum = cur_sum + candidates[i] 

            # One(or Many) times we take a Current Element
            self.backtrack(n, candidates, res, cur_comb, i, target, cur_sum)

            # BACKTRACK
            cur_comb.pop()
            cur_sum = cur_sum - candidates[i] 

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        # Sorting the Given Array
        candidates.sort()

        res = []
        cur_comb = []
        start_idx = 0
        cur_sum = 0
        self.backtrack(n, candidates, res, cur_comb, start_idx, target, cur_sum)
        return res

# -----------------------------------------------------------------------------------------

# Method 2 - No Need of Sorting

class Solution:
    def backtrack(self, n, candidates, res, cur_comb, cur_sum, target, idx):
        # Base Case
        if cur_sum == target:
            res.append(cur_comb[::])
            return
        # As we are taking Same Element Multiple Times,, Cur_Sum Will exceed Target many times
        if cur_sum > target:
            return

        for i in range(idx, n):
            # Take
            cur_sum = cur_sum + candidates[i]
            cur_comb.append(candidates[i])

            # Recursively Call with Same Ele
            self.backtrack(n, candidates, res, cur_comb, cur_sum, target, i)

            # BackTrack
            cur_sum = cur_sum - candidates[i]
            cur_comb.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        cur_comb = []
        cur_sum = 0
        start_idx = 0
        self.backtrack(n, candidates, res, cur_comb, cur_sum, target, start_idx)
        return res

# -----------------------------------------------------------------------------------------

# Method 3: 
# Many Parameters are Static in Recursive Calls
# Let's use OOPS to make them Global

