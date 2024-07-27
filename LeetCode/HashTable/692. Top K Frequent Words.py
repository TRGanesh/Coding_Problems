'''
Link : https://leetcode.com/problems/top-k-frequent-words/description/
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
'''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        '''    
        - Now the Map is created
        - Main thing is to Sort based on Freq(Higher to Lower) & 
            - Have to Maintain the Alphabetical Order(Lower to Higher)
        - Soo,, to Sort based on 2 Things,, we need to pass a Tuple in Lambda
        - Also,, We can't use 2 different values for "reverse" parameter like 
             key = lambda key: ( d[key], key ) 
             reverse = (True, False) 
        - We want to Sort based on Higher Freq 1st & Lower Word 1st
        - For that,, as same as Heap Syntax,, we are using "Negative Value" --> - d[key]
        '''
        keys_sorted = sorted(d.keys(), key = lambda key:( -d[key], key ), reverse=True)

        return keys_sorted[::-1][:k]

