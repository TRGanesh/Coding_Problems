'''
Problem Link : https://practice.geeksforgeeks.org/contest/job-a-thon-34-hiring-challenge/problems

You are given a non-negative integers array arr of length n. 
You have to remove minimum number of elements from the array such that MEX value of the updated array is not equal to the MEX value of the original array.
If it is not possible to update the MEX value then return -1.

Note:
1. MEX is the smallest non-negative number that is not present in the array.
2.MEX of an empty array will be 0.

Example 1:
Input:
n = 6
arr = {0,1, 2, 2, 3, 5}
Output:
1
Explanation:
If we remove 3 from the array then MEX value of updated array will be 3 , which is not equal to original array's MEX(i.e. 4). 
So after removing one element, we can update the MEX of the array.

Example 2:
Input:
n = 4
arr = {1, 2, 3, 4}
Output:
-1
Explanation:
MEX value of the given array is 0 and after removing any number of elements we can't change the MEX value. So answer is -1
'''
# ****************************************** Explanation with Example *************************************
'''
- 1st Realization is the Elements which are present in the Arr are bounded by the Size
- Means Max of Arr does not exceed N
- Then we can take an CountArray whose size is exactly N
- And Index of that CountArray is the exact element in the given Arr
- Values of the CountArray are the Frequencies of each element

Ex1 : [0, 1, 2, 2, 3, 5]
- CountArray : [1, 1, 2, 1, 0, 1]
        {
            As in the given Arr 
            0 is repeating 1 time,
            1 is repeating 1 time,
            2 is repeating 2 times,
            3 is repeating 1 time & 
            5 is repeating 1 time
        }
- We can see that at Index 4 of CountArray,, there is 0 Means 4 is not present in the Original Arr
- So, Now we got the MEX for the Given Arr i.e 4
- Next Question is,, Will you remove 5 from original Arr to get some other MEX ?? Ans) NO
    - Because if we remove 5 from the Original Arr the MEX not changes stays as 4
- So,, we have to remove the value which is less than 4,, Okay then,,
- Can we use this CountArray for finding the element whose removal will gives other MEX?? Ans) Yes
- But We want number of removals !!
- While traversing CountArray,, I can say like
    - I will take Element 0(Index) which is repeating 1 time,, So by removing 1 element MEX changes
    - OR I will take Element 1(Index) which is repeating 1 time,, So by removing 1 element MEX changes
    - OR I will take Element 2(Index) which is repeating 2 time,, So by removing 2 elements MEX changes
    - OR I will take Element 3(Index) which is repeating 1 time,, So by removing 1 element MEX changes
    - OR I will take Element 4(Index),,, But Wait At Index 4 there is 0,, So no need to consider further
- So,, We can the Minimum Frequency

Ex2 : [0, 0, 1, 1, 1, 3, 3, 3, 4, 4, 5]
- Maybe we can see the size of the CountArray will be based on the Maximum value of the given Arr
- CountArray : [2, 3, 0, 3, 2, 1]
        {
            As in the given Arr 
            0 is repeating 2 times,
            1 is repeating 3 times,
            2 is repeating 0 times,
            3 is repeating 3 time, 
            4 is repeating 2 times & 
            5 is repeating 1 time
        }
- In CountArray at Index 2 there is 0 means MEX of given Arr is 2
- Soo, by removing the elements which are greater than 2 does not change MEX
- While traversing CountArray,, I can say like
    - I will take Element 0 which is repeating 2 time,, So by removing 2 elements MEX changes
    - OR I will take Element 1 which is repeating 3 time,, So by removing 3 elements MEX changes
- - So,, Among them we take Minimum Frequency
'''
# Method 1
from typing import List
class Solution:
    def modifyMEX(self, n : int, arr : List[int]) -> int:
        maxi = max(arr) # Getting Max. of Given Arr,,, which is used as Size for CountArray
        
        # For some test cases,, IndexError is coming
        # For that Considering the Bigger among Maxi & n
        big_size = maxi if maxi > n else n
        
        countArray = [0] * (big_size+1)
        # Updating the CountArray with Frequencies
        for i in range(n):
            idx = arr[i]
            countArray[idx] += 1

        # Getting the MEX for Given Arr
        givenArrayMEX = 0
        for ele, freq in enumerate(countArray):
            if freq == 0:
                givenArrayMEX = ele
                break
        
        # We traverse upto that givenArrayMEX,, because Traversing beyond not changes MEX
        minMEX_after_removal = float('inf')
        for ele in range(0, givenArrayMEX):
            freq = countArray[ele]
            minMEX_after_removal = min(minMEX_after_removal, freq)
        
        if minMEX_after_removal != float('inf'):
            return minMEX_after_removal
        else:
            return -1
# -----------------------------------------------------------------------------------------------            
# Method 2:/
from typing import List
class Solution:
    def modifyMEX(self, n : int, arr : List[int]) -> int:
        maxi = max(arr) # Getting Max. of Given Arr,,, which is used as Size for CountArray
        # For some test cases,, IndexError is coming
        # For that Considering the Bigger among Maxi & n
        big_size = maxi if maxi > n else n
        
        countArray = [0] * (big_size+1)
        # Updating the CountArray with Frequencies
        for i in range(n):
            idx = arr[i]
            countArray[idx] += 1

        minMEX_after_removal = float('inf')
        # We can simply traverse the CountArray until we see freq as 0
        for ele, freq in enumerate(countArray):
            if freq == 0:
                break
            minMEX_after_removal = min(minMEX_after_removal, freq)
        
        if minMEX_after_removal != float('inf'):
            return minMEX_after_removal
        else:
            return -1
