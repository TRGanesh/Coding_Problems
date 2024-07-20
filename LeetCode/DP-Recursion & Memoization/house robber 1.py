'''
Link : https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
  the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected &
  it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, 
  return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''


'''
- There can be 2 Ways,, Alternatively
- Idea failed for [2,1,1,2]
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        num_houses = len(nums)
        
        way_1 = 0 # Take 0th house & Then Alternatively
        way_2 = 1 # Take 1st house & Then Alternatively

        price1, price2 = 0, 0

        ans1 = float('-inf')
        ans2 = float('-inf')

        path1, path2 = [], [] # Store Paths,,for testing
        while way_1 < num_houses:
            price1 += nums[way_1]
            path1.append(way_1)
            
            ans1 = max(ans1, price1)
            
            way_1 += 2
        
        while way_2 < num_houses:
            price2 += nums[way_2]
            path2.append(way_2)
            
            ans2 = max(ans2, price2)
            
            way_2 += 2

        return max(ans1, ans2)

# --------------------------------------------------------------------

'''
Why DP:
- There are Options for each House(Either can Rob/Not Rob)
- Asked for Optimal Answer
- There are Overlapping Sub-Problems
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        def recur(i):
            # i --> Iterator/House Number
            if i >= num_houses: # ">=" not ">"
                return 0

            # If already in Memo
            if i in memo:
                return memo[i]

            # Take ith House --> Consider Current House & Call for i+2 th House
            # if i + 2 < num_houses:
            take_i = nums[i] + recur( i+2 )
        
            # Not Take ith House --> Don't Consider Current House & Call for i+1 th House
            # if i + 1 < num_houses:
            not_take_i = recur( i+1 )

            memo[i] = max(take_i, not_take_i)

            return memo[i]

        # Main
        num_houses = len(nums)
        memo = {}

        return recur(0)
