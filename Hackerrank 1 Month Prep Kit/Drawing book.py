'''
Link : https://www.hackerrank.com/challenges/one-month-preparation-kit-drawing-book/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two
'''
************ wrong ***************
def pageCount(n, p):
    # Number of Jumps needed from the first page
    turns_from_front = p // 2
    print('turns_from_front', turns_from_front)
    
    # from_last_page = ((n - p) // 2) + 1 // Wrong
    # Let's do Loop for Last
    i = n
    turns_from_last = 0
    if n % 2 != 0:
        # At a Time,, we can look a Even Page_Num & Odd Page_Num
        # If p == Even Page_Num,, No need to Filp
        if n - 1 == p:
            turns_from_last = 0
            return min(turns_from_front, turns_from_last)
    
    while i > p:
        turns_from_last += 1
        i = i - 2
    print('from_last_page', turns_from_last)
    
    return min(turns_from_front, turns_from_last)

# above code is positive for some test cases but not all because
# - for counting number of turns_from_last we are looping,, but what we can do is,,
# - we can do subtract the turns_from_front from the total number of turns(to reach end)

def pageCount(n, p):
    # Number of Jumps needed from the first page
    turns_from_front = p // 2
    print('turns_from_front', turns_from_front)
    
    total_turns_to_reach_last = n // 2
    
    if n % 2 != 0 and p == n - 1:
        # "P" is at Last Page
        return 0
    
    else:
        turns_from_last = total_turns_to_reach_last - turns_from_front
    
    return min(turns_from_front, turns_from_last)
