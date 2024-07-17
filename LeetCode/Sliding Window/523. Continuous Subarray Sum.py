'''
Problem Link : https://leetcode.com/problems/continuous-subarray-sum/description/

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where:
  --> its length is at least two, and
  --> the sum of the elements of the subarray is a multiple of k.
Note that:
- A subarray is a contiguous part of the array.
- An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 
Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
'''
'''
- If we use Sliding Window Technique then when to add element into the window && when to delete element from the window is a little bit tricky to understand

- Math Concept:
Ex: n = 31, k = 4
    31 % 4 = 3,,
    Then,, if we add any multiple of 4 to 31 the remainder will be same

- we will apply the same concept as Prefix Sum
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        if n < 2:
            return False
        
        # This Map stores the remainder for the Running Sum
        remainder_idx_map = {0:-1}

        running_sum = 0

        for i in range(n):
            running_sum += nums[i]

            remainder = running_sum % k

            if remainder not in remainder_idx_map: # running_sum >= k Wrong Condition
                remainder_idx_map[remainder] = i
            
            elif remainder in remainder_idx_map:
                if (i - remainder_idx_map[remainder]) >= 2:
                    # Checking the size of the SubArray
                    return True

            if remainder % k == 0:
                if (i - remainder_idx_map[remainder]) >= 2:
                    return True
                 
        return False
