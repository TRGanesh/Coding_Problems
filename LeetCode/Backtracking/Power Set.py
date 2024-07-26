'''
Link : https://www.geeksforgeeks.org/problems/power-set4302/1
'''
# Tree-Diagram Link : https://www.researchgate.net/profile/Patrick-Prosser/publication/229329300/figure/fig2/AS:670027082641412@1536758313538/A-binomial-search-tree-producing-the-power-set-of-0-1-2-3.png
'''
- There are 2 options,, pick & not_pick. But also have to follow Sequence of Appearance
- There will be a Current Forming SubSet
'''

def AllPossibleStrings(self, s): # TC : O(n * 2^n)
  def getAllSubsets(s, cur_subset, idx, all_subsets):
      if idx >= len(s):
          if len(cur_subset) >= 1:
              all_subsets.append(''.join(cur_subset[::]))
          return

      '''
      if idx >= len(s) and len(cur_subset) >= 1:
          all_subsets.append(''.join(cur_subset[:]))
          return 
      '''
      '''
      for i in range(idx, len(s)):
          cur_subset.append(s[i])
          getAllSubsets(s, cur_subset, i+1)
          cur_subset.pop()
      '''
     
      cur_subset.append(s[idx])
      getAllSubsets(s, cur_subset, idx+1, all_subsets)
      cur_subset.pop()
      getAllSubsets(s, cur_subset, idx+1, all_subsets)
        
  
  all_subsets = []
  cur_subset = []
  idx = 0
  
  getAllSubsets(s, cur_subset, idx, all_subsets)
  
  all_subsets.sort()
# 		print(all_subsets)
  
  return all_subsets
