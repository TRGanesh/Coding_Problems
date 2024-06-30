'''
problem link : https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/

A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
Example 2:

Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
Example 3:

Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.
'''

# Method 1
# BRUTE - TLE  - O(n^2)
'''
- Let's consider each position in the string as the starting point of a potential segment/subString of consecutive 'T's or 'F's
- We have to try for both possibilities,, To Maximize T's & To Maximize F's
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)

        maxConsecutiveT = 0 
        maxConsecutiveF = 0

        # Trying to Maximize T's
        # Here,, we try to Count F's & If that count is <= k,, then we update the maxConsecutiveT with Current SubString Length
        # We are using "<=" because in problem they said "performing the operation `at most k` times"
        for i in range(n):
            count_F = 0 # Number of F's for Current SubString
            # If Count_F becomes more/equal than K,, then that SubString may be our answer
            for j in range(i, n):
                if answerKey[j] == 'F':
                    count_F += 1
                if count_F <= k:
                    subStr_len = j - i + 1
                    maxConsecutiveT = max( maxConsecutiveT, subStr_len )
        
        # Trying to Maximize F's
        for i in range(n):
            count_T = 0 # Number of T's for Current SubString
            # If Count_T becomes more/equal than K,, then that SubString may be our answer
            for j in range(i, n):
                if answerKey[j] == 'T':
                    count_T += 1
                if count_T <= k:
                    subStr_len = j - i + 1
                    maxConsecutiveF = max( maxConsecutiveF, subStr_len )
        
        return max(maxConsecutiveF, maxConsecutiveT)
# ----------------------------------------------------------------------------------------
# Method 2 
# SLIDING WINDOW - TC : O(n)
'''
- In Brute Force,, One time we tried for Maximizing T's & Other time for F's
- In Similar Fashion, We do Repeat Sliding Window for 2 times
'''
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        n = len(answerKey)
        
        maxConsecutiveT = 0
        maxConsecutiveF = 0

        # Trying to Maximize T's
        # If Adding Char is F,,then increment count_F
        left, right = 0, 0 
        count_F = 0
        while right < n:
            
            if answerKey[right] == 'F':
                count_F += 1
            
            while count_F > k:
                # We have to Shrink the Window
                if answerKey[left] == 'F':
                    count_F -= 1
                left += 1

            if count_F <= k:
                    subStr_len = right - left + 1
                    maxConsecutiveT = max( maxConsecutiveT, subStr_len ) 
            
            right += 1
        
        # Trying to Maximize F's
        # If Adding Char is T,,then increment count_T
        left, right = 0, 0  # Re-Initializing Left & Right is compulsory
        count_T = 0
        while right < n:
            
            if answerKey[right] == 'T':
                count_T += 1
            
            while count_T > k:
                # We have to Shrink the Window
                if answerKey[left] == 'T':
                    count_T -= 1
                left += 1 
            
            if count_T <= k:
                    subStr_len = right - left + 1
                    maxConsecutiveF = max( maxConsecutiveF, subStr_len )
            
            right += 1

        return max(maxConsecutiveF, maxConsecutiveT)
# ----------------------------------------------------------------------------------------
# Method 3 - Using Helper Function
# Soo, why to write 2 same Blocks of code twice !!

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(answerKey, char):
            n = len(answerKey)
            left, right = 0, 0 
            max_len = 0

            # If Current Char is T,,then we have to Count for F & If Current Char is F,,then we have to Count for T
            if char == 'T':
                opposite_char = 'F'
            else:
                opposite_char = 'T'
            
            # opposite_char = 'F' if char == 'T' else 'T'

            oppositeChar_count = 0 # Stores count of Opposite Char in Window
            while right < n:
                # Add Right Pointer into Window
                if answerKey[right] == opposite_char:
                    oppositeChar_count += 1
                
                # Shrinking Window
                while oppositeChar_count > k:
                    if answerKey[left] == opposite_char:
                        oppositeChar_count -= 1
                    left += 1
                
                if oppositeChar_count <= k:
                    max_len = max( max_len, right - left + 1 )

                right += 1 
            return max_len

        return max(maxConsecutiveChar(answerKey,'F'), maxConsecutiveChar(answerKey,'T'))

# Final Thoughts:
'''
- OfCourse as this problem belongs to SubStrings(consecutive chars of a string),, we should try for All SubStrings(Brute Force)
- Here for a Char,, there are 2 Possibilities which we can do
    - If Char is T, change to F & Inverse
- So, We have to give equal importance to each T & F
- Due to that we have written the same code for both of them & at last compared
- In Method 3, we used Helper function that also Generalized(works for both T & F)
'''







