'''
Link : https://www.hackerrank.com/challenges/one-month-preparation-kit-zig-zag-sequence/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two
'''

def zigzag_sequence(arr):
    n = len(arr)
    arr.sort()
    mid = int((n + 1) / 2) - 1
    # As after the Middle Guy,, all guys will be greater than that guy
    
    # Swap middle element with the last element
    arr[mid], arr[-1] = arr[-1], arr[mid]
    
    # Reverse the second half to form the decreasing sequence
    # No need to Consider about the 1st Half
    
    left = mid + 1
    right = n - 2
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr
