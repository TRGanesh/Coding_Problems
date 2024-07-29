'''
Link : https://www.hackerrank.com/challenges/one-month-preparation-kit-tower-breakers-1/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two
'''

'''
- Q) Always we should expect the Bad scenario from the Player 2 ???? 
- When reducing the height of a tower, the new height must be a proper divisor of the current height
Base Case:
- If the height of a tower is 1, it cannot be reduced further.
- If all towers have a height of 1 at the start, Player 1 cannot make any move and loses immediately.
- If number of towers equals 1 and height of Tower is greater than 1,then player 1 will reduce the height of that single tower to 1 and immediately player 2 will lose
Main thing:
- Up to which height you can reduce,, such that if opposite player will come and look he will not able to reduce further
- So possible things are 1 <= Y < X,, and Y should evenly divide X
- That means the possible things are the Proper Divisors of X
    - Okay,, a number can have many Divisors,, but 1 is the compulsory
- Soo, don't think too much if current height is say "m" and there are some "n" towers,,
    - Who ever will go they will make 1 tower to height 1
    -If all towers have height one then we cannot reduce further
- so finally it completely depends on the total number of towers either odd or even
'''
def towerBreakers(n, m):
    num_towers = n
    height = m
    
    if height == 1: # not further reducible
        return 2
    
    if num_towers == 1 and height > 1:
        # As only single tower player 1 makes its height 1 and player 2 cannot reduce further so player 1 won
        return 1
    
    if num_towers % 2 == 0: # Even 
        return 2
    else: # Odd
        return 1 
    
    return 1
