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

# Simple & Clean Code
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(cur_comb, idx, target):
            if target == 0:
                res.append(cur_comb[::])
                return
            if target < 0:
                return
            
            for i in range(idx, n):
                cur_comb.append(candidates[i])
                backtrack(cur_comb, i, target - candidates[i])
                cur_comb.pop()
        
        n = len(candidates)
        res = []
        backtrack([], 0, target)
        return res

# -------------------------------------------------------------------------------------------------------------

# Method 1 - Involves Sorting

class Solution:
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

# -----------------------------------------------------------------------------------------

# Method 2 - No Need of Sorting

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        cur_comb = []
        cur_sum = 0
        start_idx = 0
        self.backtrack(n, candidates, res, cur_comb, cur_sum, target, start_idx)
        return res
    
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

# -----------------------------------------------------------------------------------------

# Method 3: ******** May be SomeWhat Confusing If you don't know Object-Oriented Programming in Python **********
# Many Parameters are Static in Recursive Calls
# Let's use OOPS to make them Global

class Solution:
    def __init__(self):
        self.n = 0
        self.target = 0
        self.res = []
        self.candidates = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.n = len(candidates)
        self.target = target
        self.res = []

        cur_comb = [] # Not Global
        start_idx = 0
        
        self.backtrack(cur_comb, start_idx)
        
        return self.res
    
    def backtrack(self, cur_comb, idx):
        # Base Cases
        if self.target == 0:
            self.res.append(cur_comb[::])
            return 
        if self.target < 0:
            return
        
        for i in range(idx, self.n):
            # Take
            cur_comb.append(self.candidates[i])
            self.target = self.target - self.candidates[i]

            # Recursion
            self.backtrack(cur_comb, i)

            # Backtrack
            cur_comb.pop()
            self.target = self.target + self.candidates[i]

# Final Thoughts:
'''
- Main Variation in 4 Methods is the Code structure, like how will you pass the parameters, how do you update them
- Whether do you moodify the Target in Recursion Or use a Current_Sum (denoting sum of Current_Combination)
- In Backtracking cases,, Modifying(Appending) the List into a List should include Shallow Copy in Python
- In Method 3,, We used Default Constructor to Initialize the Variables which are needed 
    - Even when we are writing Code for real-world applications,, OOPS is very important
'''
