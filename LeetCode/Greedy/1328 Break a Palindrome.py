'''
problem link: https://leetcode.com/problems/break-a-palindrome/description/ 

Given a palindromic string of lowercase English letters palindrome, 
  replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. 

If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, 
  a has a character strictly smaller than the corresponding character in b. 

For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

Example 1:
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.

Example 2:
Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string
'''

'''
- Ex: "aaaa"
- At that time,,, we want to change the Last "a",, such that we get Lexicographically smaller 
- so if we have a series of "a"s then just move i ptr until last "a" & change to "b"
- For odd length palindrome,, if you change the mid guy,, then also it stays as plaindrome
    Ex : "aabaa" --> if you change "b" to "a",,then also it stays as plaindrome
    - In above Ex,, as we can't change the chars,, then convert last char to "b"
- For strings like "abccba",, we just have to look at n/2 part 
- For Odd like "abcba",, then also just traverse 1st half,,
    - If you did not made any changes in 1st half,, then simply change last char to "b"

- Have to realize that,, if not able to change things in 1st part,, then Can't do in 2nd half also. So have to change last char to 'b'
'''

class Solution:
    def breakPalindrome(self, p: str) -> str:
        n = len(p)
        l = list(p)
        if n == 1:
            return ""

        if n > 1 and l[0] != 'a':
            l[0] = 'a'
            return ''.join(l)

        isChanged = False

        for i in range( 0, (n//2) ):
            print(l[i])

            if l[i] != "a":
                l[i] = "a"
                isChanged = True
                break
        
        if isChanged == False:
            l[-1] = 'b'
        
        return ''.join(l)


''' Initial Try --> Okay
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        def check(l):
            return l != l[::-1]

        isChanged = False
        l = list(palindrome)

        for i in range(0,len(l)):
            if i == 0 and l[i] == 'a':
                pass
            
            if i == 0 and l[i] != 'a':
                t = l[i]
                l[i] = 'a'

                if check(l):
                    isChanged = True
                    break
                else:
                    l[i] = t  

            # "aaa"
            while i < len(l) and l[i] == 'a':
                i = i + 1
            
            i = i - 1
            l[i] = 'b'
            if check(l):
                    isChanged = True
                    break
            else:
                l[i] = 'a'              
            
            if i != 0 and l[i] == 'a':
                l[i] = 'b'

                if check(l):
                    isChanged = True
                    break
                else:
                    l[i] = 'a'
            
            if i != 0 and l[i] != 'a':
                t = l[i]
                l[i] = 'a'

                if check(l):
                    isChanged = True
                    break
                else:
                    l[i] = t

        if isChanged:
            return ''.join(l)
        return ""
'''
