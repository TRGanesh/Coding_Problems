'''
Problem Link: https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1
Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

Example 1:
Input:
txt = forxxorfxdofr
pat = for
Output: 3
Explanation: for, orf and ofr appears
in the txt, hence answer is 3.

Example 2:
Input:
txt = aabaabaa
pat = aaba
Output: 4
Explanation: aaba is present 4 times
in txt.
'''

# Brute - TLE
from collections import Counter
class Solution:
	def search(self,pat, txt):
	    m = len(txt)
	    n = len(pat)
	    pat_map = Counter(pat)
	    
	    ans = 0
	    for i in range(m):
	       #print(txt[i:i+n])
	       sub_str = txt[i : i+n]
	       if Counter(sub_str) == pat_map:
	           ans += 1
	   
	    return ans
# -------------------------------------------------------
from collections import Counter
class Solution:
	def search(self,pat, txt):
	    m = len(txt)
	    n = len(pat)
	    pat_map = Counter(pat)
	    
	    i, j = 0, 0
	    ans = 0
	    
	    while j < m:
	       # Update j th Char in Map,,as Incusion
	       if txt[j] in pat_map:
	            pat_map[ txt[j] ] -= 1
	           
	       cur_window_size = j - i + 1
	       if cur_window_size == n:
	           # Check whether Map has all Values as Zero or Not
	           all_zero = True
	           for val in pat_map.values():
	                if val != 0:
	                    all_zero = False
	           
	           if all_zero == True:
	               ans += 1
	           
	           # Move i pointer
	           # Update i th Char in Map,,as Exclusion
	           if txt[i] in pat_map:
	            pat_map[ txt[i] ] += 1
	            
	           i += 1
	       j += 1
	   
	    return ans
