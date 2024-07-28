'''
Link : https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two
'''

from collections import Counter
def sockMerchant(n, ar):
    colors_map = Counter(ar)
    
    ans = 0
    for color, val in colors_map.items():
        if val < 2:
            continue
        elif val == 2:
            ans += 1 
        elif val > 2:
            num_of_pairs = val // 2
            ans += num_of_pairs
    
    return ans
