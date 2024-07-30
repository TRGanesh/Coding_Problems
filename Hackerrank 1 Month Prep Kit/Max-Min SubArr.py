'''
Link: https://www.hackerrank.com/challenges/one-month-preparation-kit-angry-children/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two
'''

'''
- We have to Consider all SubArrays of Length "k"
- Q) In question did they mentiond Sub-Arr ????
'''
# TC : O(n ^ 2)
def maxMin(k, arr):
    arr.sort() # May be Sorting is Compulsory as Removing it made more Errors in Cases
    
    mini = float('inf')
    for i in range(0, len(arr) - k):
        sub_arr = arr[i:i+k]
        mini = min( mini, (max(sub_arr) - min(sub_arr)) )
        
    return mini
# --------------------------------------------------------------
def maxMin(k, arr):
    arr.sort() # May be Sorting is Compulsory as Removing it made more Errors in Cases
    
    mini = float('inf')
    left, right = 0, k-1
    window_max = float('-inf')
    window_min = float('inf')
    
    while right < len(arr):
        window_min = arr[left]
        window_max = arr[right]
        
        mini = min(mini ,window_max - window_min)
        left += 1
        right += 1
        
    return mini
