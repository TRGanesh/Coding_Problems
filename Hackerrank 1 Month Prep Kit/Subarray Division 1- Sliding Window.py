'''
Link: https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
'''

def birthday(s, d, m):
    window_size = m
    window_sum = d
    
    left, right = 0, 0
    ans = 0
    cur_window_sum = 0
    
    while right < len(s):
        cur_window_sum += s[right] 
        
        if right - left + 1 > window_size: 
            # Move Window by 1 Step
            cur_window_sum -= s[left]
            left += 1
        
        if cur_window_sum == window_sum and (right - left + 1 == window_size):
            # Extra And Condition is solved some other test cases
            ans += 1
        right += 1 
    
    return ans
