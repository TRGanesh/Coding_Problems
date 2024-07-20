'''
Link : https://leetcode.com/problems/house-robber-ii/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, && 
  it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
'''

# Method 1 : Recursion + Memo
'''
- As 1st House & Last House have a Connection,,
- We can simply do consider for 2 cases
  - One Stolen 1st House & Other Stolen Last House
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        def recur(nums ,i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            take_i = nums[i] + recur(nums, i+2)
            not_take_i = recur(nums, i+1)

            memo[i] = max(take_i, not_take_i)
            return memo[i]

        n = len(nums)

        if n < 2:
            return nums[0]
        
        # Case 1: Stolen 1st House,, then Consideration area should be [0: n-1]
        memo = {}
        case1 = recur(nums[0 : n-1], 0)

        # Case 2: Stolen Last House,, then Consideration area should be [1:n]
        memo = {}
        case2 = recur(nums[1 : n], 0)

        return max(case1, case2)
# ----------------------------------------------------------------------
