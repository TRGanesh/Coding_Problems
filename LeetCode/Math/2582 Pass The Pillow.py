'''
Problem Link: https://leetcode.com/problems/pass-the-pillow/description/
There are n people standing in a line labeled from 1 to n. 
The first person in the line is holding a pillow initially. 
Every second, the person holding the pillow passes it to the next person standing in the line. 
Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

Example 1:
Input: n = 4, time = 5
Output: 2
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
After five seconds, the 2nd person is holding the pillow.

Example 2:
Input: n = 3, time = 2
Output: 3
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
After two seconds, the 3rd person is holding the pillow.
'''

# Method 1: Using Simulation - TC: O(time)
'''
Main Considerations:
- We have to Take care about the Direction Changes

Simulation : Just to do what Asked
- We traverse the people for "time" number of seconds
- When the pillow pointer reaches the boundaries then we have to change the direction
- Whenever you move the pillow pointer at the same time decrement the time
'''
def passThePillow(self, n: int, time: int) -> int:
    pillow_ptr = 1 # Index of the Pillow after time seconds
    
    # if number of people are greater than the given time,,
    if n > time:
        # We can simply pass on the Pillow without changing the Direction
        for pillow_idx in range(1,time+1):
            pillow_ptr += 1
        return pillow_ptr

    # Direction Changes will happen when time is greater than n
    direction = 1
    while time:
        '''
        - Move the pillow_ptr Until you not cross boundary
        - Means pillow_ptr is in b/w the boundaries
        - Soo, range of pillow_ptr should be [1,n]
        '''
        if pillow_ptr >= 1 and pillow_ptr <= n:
            pillow_ptr = pillow_ptr + direction
            time -= 1

        # Due to above If Condition,,it also considers Moving Pillow when Pillow is at 1 or n
        # Soo,, pillow_ptr will becomes 0 or n+1
        # Handling those cases
        if pillow_ptr < 1:
            pillow_ptr = 1
        if pillow_ptr > n:
            pillow_ptr = n
        
        # Change Direction,, as we reached the boundaries
        if pillow_ptr == n or pillow_ptr == 1:
            direction = direction * -1
        
    return pillow_ptr

# ---------------------------------------------------------------------------------------------------
# Method 2: Using Simulation - TC: O(time)
# In Method 1, we handled the n > time case separately
# But with the While loop itself it gets handles,, also we can make sure to handle the pillow_ptr crossing boundary edge case more simply

def passThePillow(self, n: int, time: int) -> int:
    pillow_ptr = 1 # Initially pillow is it 1st guy
    direction = 1 # 1 denotes left to right direction

    while time:
        if (pillow_ptr + direction >= 1) and (pillow_ptr + direction <= n):
            pillow_ptr = pillow_ptr + direction
            time = time - 1
        
        if pillow_ptr == n or pillow_ptr == 1:
            direction = direction * -1
    
    return pillow_ptr
# ---------------------------------------------------------------------------------------------------

'''
# Method 3: Using Math - TC: O(1)
- If there are 5 people,, then number of steps required to cover one complete traversal in one direction is n-1 i.e 4

Ex: n = 5, time(t) = 6
    -- t = 0 , pillow_ptr = 1 (Not Considerable,,as initial case)
    -- t = 1 , pillow_ptr = 2
    -- t = 2 , pillow_ptr = 3
    -- t = 3 , pillow_ptr = 4
    -- t = 4 , pillow_ptr = 5
    -- t = 5 , pillow_ptr = 4
    -- t = 6 , pillow_ptr = 3

- We have to realise that there will be some complete traversals and one in-complete traversal
- In above example,, 
    - from time = 0 to time = 4,, it's a complete traversal
    - from time = 5 to time = 6,, it's a in-complete traversal
- time_remained(after complete traversals) = total_time - (number of complete rounds) * (steps for each round)
- Q) How many Complete Rounds will be there?
  Ans) As each round has n-1 steps,, time / (n-1) gives complete rounds
- time_remained(after complete traversals) = total_time - (total_time/(n-1)) * (n-1)
- If number of complete rounds is odd that means, pillow_ptr is at n
- If number of complete rounds is even that means, pillow_ptr is at 1
- From that position,, we have to take time_remained number of steps
'''
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pillow_ptr = 1
        stepsPerRound = n - 1
        numOfCompleteTraversals = time // stepsPerRound
        timeRemainedAfterCompleteTraversals = time - (numOfCompleteTraversals * stepsPerRound)

        if numOfCompleteTraversals % 2 == 0:
            # Even means,, pillow_ptr is at 1,, 
            # So move from 1 to timeRemainedAfterCompleteTraversals number of teps
            return 1 + timeRemainedAfterCompleteTraversals
        
        elif numOfCompleteTraversals % 2 != 0:
            # Odd means,, pillow_ptr is at n,, 
            # So move from n to timeRemainedAfterCompleteTraversals number of teps in backwards
            return n - timeRemainedAfterCompleteTraversals
