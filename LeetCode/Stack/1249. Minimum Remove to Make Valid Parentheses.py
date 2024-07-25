'''
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
'''


'''
- What will you Store in Stack?? Either Exact Paranthesis or Index
- For Proper Deletion of Un-Balanced Paranthesis,, we have to store the Indices
- Stack holds the Indices where Un-Balanced Paranthesis are present
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            
            elif char ==')':
                # Check whether Stack is Empty or Not
                # && Check for Corresponding "("
                if not stack:
                    # If Empty,, then Simply Push the ")" Index,, as that Index is Un-Balanced
                    stack.append(i)
                
                elif s[stack[-1]] == ')':
                    # Or,, If Stack's Top guy is ")",,and Current Char is also ")",, then Simply Push Current Index too
                    stack.append(i)
                
                elif stack and s[ stack[-1] ] == '(':
                    # Matching Found,, then Pop
                    stack.pop()
            
            else:
                continue

        unbalanced_paranthesis_idxs = [0]*len(s)
        
        for i in range(len(stack)):
            idx = stack[i]
            unbalanced_paranthesis_idxs[idx] = 1
        
        ans = ""
        for i in range(len(s)):
            if unbalanced_paranthesis_idxs[i] != 1:
                ans += s[i]
        
        return ans
