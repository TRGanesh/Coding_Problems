'''
Link : https://leetcode.com/problems/house-robber-iii/description/

The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called root.
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that all houses in this place form a binary tree. 
It will automatically contact the police if two directly-linked houses were broken into on the same night.
Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

'''

'''
- If you are at a Node,, then if you pick it's value then cannot pick it's child values
- Let's say you are at Child,, then 2 Options(pick, not pick)
    - If Picked,, then consider it's value
    - If not Picked,, then don't consider
- Okay,, what kind of traversal will you do??
    - Left & Right & then Root(Parent)
- For a node,, it will be getting result from Left Sub-Tree, Right Sub-Tree & has a comparision with it's own value
- Also,, at a Parent node,, there will be 2 Options,, Pick/Not Pick
    - If Pick,, then no need to Add Left & Right Side Results
    - If not Pick,, then Add Left & Right Sub-Trees 

- For each Node,, there will be 2 Values,,for picking & not picking
- If you are parent,, and picking the parent,, then we have to consider not-picking values for left & right childs
- If you are not picking parent,, then 
    - It's free of choosing from picking & not picking values from child

- Let's say 'P' is Parent & L is Left & R is Right child
    --> pick_P = P.val + not_pick_L + not_pick_R
    --> not_pick_P = max(pick_L, not_pick_L) + max(pick_R, not_pick_R)
- Soo, for every node,, there are 2 Values,, Soo let's store them in a list
'''

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node == None:
                # Return 0, 0 denoting no money to rob
                return [0, 0]
            
            # Call for Left Side
            left_side_results = dfs(node.left)
            # Call for Right Side
            right_side_results = dfs(node.right)

            pick_node = node.val + left_side_results[1] + right_side_results[1]
            not_pick_node = max(left_side_results[0], left_side_results[1]) + max(right_side_results[0], right_side_results[1])

            return [pick_node, not_pick_node]
        
        options = dfs(root)
        return max(options[0], options[1])
