Leetcode Problem Link : https://leetcode.com/problems/delete-and-earn/description/

'''
Problem Statement
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.
'''

from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo = {}

        def getMaxPoints(ele):
            '''
            - Ofcourse as this is a Recursive Func,, we try for each value from "element to 0"
            - And,, that Element should present in Map / Nums Array
            - For An Ele,, We do 2 Things
                1. One time Consider that Element & It's Points
                2. Don't Consider that Element
            - If we Consider current Element,, then have to Not Consider "Element + 1" & "Element - 1"
                - As We are making Recursive call from Max_Ele of Nums,,So No Need to Worry about "Ele + 1"
            - If We Don't consider,, then have to simply call for "Element - 1"
            '''

            # Base Cases
            if ele == 0:
                return 0 
            
            # As Recursive Calls happen,, Ele can Reach 1 / 0
            # So Handling 1 Should be done at every time without checking in Map
            # if ele in ele_TotalPoints_map and ele == 1:
            #    return ele_TotalPoints_map[ele] # ele_TotalPoints_map.get(1, 0)
            
            # Also, Each Recursive Call should happen without LookUp in Map

            if ele == 1:
                return ele_TotalPoints_map.get(ele, 0)

            if ele in memo:
                return memo[ele]

            takeN = ele_TotalPoints_map.get(ele, 0) + getMaxPoints(ele-2)
            not_TakeN = getMaxPoints(ele-1)
            max_points = max(takeN, not_TakeN)

            memo[ele] = max_points

            return max_points

        # Main
        # Total Points which are Sure for Each Single Ele is (Ele * It's Freq)
        # So, Let's get Total Points for Each Ele & Store in Map
        ele_TotalPoints_map = {key : key * freq for key, freq in Counter(nums).items()}
        
        # Now, we Call the Function for Max Ele of Nums
        max_ele = max(nums)

        return getMaxPoints(max_ele)
