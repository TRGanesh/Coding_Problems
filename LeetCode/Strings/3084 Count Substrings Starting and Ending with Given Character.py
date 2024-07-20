'''
Link : https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/description/
You are given a string s and a character c. Return the total number of  substrings of s that start and end with c.

 Example 1:
Input: s = "abada", c = "a"
Output: 6
Explanation: Substrings starting and ending with "a" are: "abada", "abada", "abada", "abada", "abada", "abada".

Example 2:
Input: s = "zzz", c = "z"
Output: 6
Explanation: There are a total of 6 substrings in s and all start and end with "z".
'''

'''
- There will be some occurences of "c",, in given string
- Soo,,, For every Current "c" we can make connections(SubStrs) with previous "c"s
- Ex : s = "abada", c = "a"
    Let i = 4,, 
    Previously "a"s are present at [0,2]
    Soo, this ith guy can make substrs with those 2 "a"s
'''

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n = len(s)
        prev_Cs = [] # List to Store the Indices of the C's
        num_of_prev_Cs = 0 # Variable just to store the Count of Previous Guys

        ans = 0
        for i in range(n):
            if s[i] == c:
                ans += 1
                ans += num_of_prev_Cs # len(prev_Cs) 
                num_of_prev_Cs += 1
                # prev_Cs.append(i)

        print(prev_Cs)
        print(ans)

        return ans 
