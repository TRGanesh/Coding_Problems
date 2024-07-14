'''
Problem Link : https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/
A critical point in a linked list is defined as either a local maxima or a local minima.
A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points &&
  maxDistance is the maximum distance between any two distinct critical points. 
If there are fewer than two critical points, return [-1, -1].

Example 1:
Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].

Example 2:
Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

Note that the last node is not considered a local maxima because it does not have a next node.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
- At first, we need to find the Positions of Critical Points
- Either we can store all those Critical Points Positions in some data structure and can do some processing on it
- Otherwise we can think about which Critical Points are Necessary/Needed for calculating the Minimum & Maximum Distance
- Maximum distance will be the distance between the first CP & the last CP
- For minimum distance we need to consider the CP's which are near to each other
- Finding the Maximum Distance is somewhat simpler
- So what we will do means, We will traverse the Linked List and if we see a CP then we will compare that position with the position of the previously seen CP
'''
def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    # Pointers denoting Previous CP Position & 1st CP Position 
    prevCPPosition = 0
    firstCPPosition = 0

    # For finding the Minimum distance,, distance between above two is compared

    # As the Boundary Nodes does not belongs to Critical Points, we have to start from Second Node
    curNode = head.next 
    # Pointer to store 0-indexing based Position of curNode
    curNodePosition = 1 

    prevNode = head # Prev Pointer for curNode

    minDist = float('inf')
    while curNode.next:
        # For a node to become a CP,, its value should be either greater or smaller than the left and the right nodes
        
        if ( (curNode.val > curNode.next.val and curNode.val > prevNode.val) or 
             (curNode.val < curNode.next.val and curNode.val < prevNode.val)
            ):
            # What if the Current CP is 1st CP,,
            if firstCPPosition == 0:
                firstCPPosition = curNodePosition
                prevCPPosition = curNodePosition
            else:
                # If current CP is not 1st then compare distance
                minDist = min(minDist, curNodePosition - prevCPPosition)
                prevCPPosition = curNodePosition
            
        # Whenever we are traversing we have to make sure to update the Current Node Position and Previous Node
        curNodePosition += 1
        prevNode = curNode
        curNode = curNode.next
        
    # After While Loop,, the prevCPPosition stays at the Last CP

    if minDist == float('inf'):
        return [-1, -1]
    else:
        maxDist = prevCPPosition - firstCPPosition
        return [minDist, maxDist]
