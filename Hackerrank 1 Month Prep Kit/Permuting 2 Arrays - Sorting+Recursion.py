'''
Link : https://www.hackerrank.com/challenges/one-month-preparation-kit-two-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
'''

# Method 1: Recursion + BackTracking - Executed for Some Cases,, Complete Naive Approach
def twoArrays(k, A, B):
    # Let's generate all Permutations - using Swapping
    def getAllPermuations(a, idx, all_perms):
        if idx >= len(a):
            all_perms.append(a[::])
            return
        
        for i in range(idx, len(a)):
            # Swap with all indices which are at right to i
            a[idx], a[i] = a[i], a[idx]
            
            # Call Recursion
            getAllPermuations(a, idx+1, all_perms)
            
            # Again Put Back --> Backtrack
            a[idx], a[i] = a[i], a[idx]
    
    n = len(A)
    
    all_perms_A = []
    getAllPermuations(A, 0, all_perms_A)
    
    all_perms_B = []
    getAllPermuations(B, 0, all_perms_B)
    
    # print(all_perms_A)
    # print(all_perms_B)
    
    # Now,, Checking if any 2 Permutations are satisfying the Condition or not
    for perm_a in all_perms_A:
        for perm_b in all_perms_B:
            is_sum_equal = True
            for i in range(n):
                if perm_a[i] + perm_b[i] < k:
                    is_sum_equal = False
                    break
            
            if is_sum_equal == True:
                return "YES"
    
    return "NO"
# ------------------------------------------------------------------------------
# Method 2: Sorting - Pairing
'''
- Sort 1 Arr in Ascending Order
- Sort other Arr in Descending Order
- Because the sum > k condition should be satisfied with all pairs,,soo we need to change the order such that
    - Sum of those 2 Elements will become Maximum
'''
def twoArrays(k, a, b):
    n = len(a)
    a.sort()
    b.sort(reverse=True)
    
    is_found = True
    for i in range(n):
        if a[i] + b[i] < k:
            is_found = False
            break
    if is_found == True:
        return 'YES'
    else:
        return 'NO'

