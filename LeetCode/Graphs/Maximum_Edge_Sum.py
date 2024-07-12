'''
Problem Link : https://practice.geeksforgeeks.org/contest/job-a-thon-34-hiring-challenge/problems

You are given an undirected tree of n nodes and n-1 weighted edges. where edges[i] = {u, v, w}, w is the weight of the edge between node u and node v.
You have to find the sum of the maximum weighted edge in all unordered paths in the tree, which have at least one edge.
Note: Unordered path means path from u to v and v to u considered same.

Example 1:
Input:
n = 3
edges = {{1,2,2} , {1,3,4}}

Output:
10

Explanation:
as we can see in the tree -
maximum weighted edge in path from 1 to 2 = 2
maximum weighted edge in path from 1 to 3 = 4
maximum weighted edge in path from 2 to 3 = max(2, 4) = 4
so sum of all maximum weighted edges = 2 + 4 + 4 = 10.
'''


'''
- A tree is a connected acyclic graph
- Any two nodes in a tree are connected by a unique path.
- In a tree with n nodes, there are n*(n-1)/2 unique pairs of nodes
- We should mainly focus on finding all Unordered paths from u to v
- In the given examples, we can see there is an Entry for every 2 nodes which are linked
- Soo, Maybe we can use a Matrix, where rows and columns represent the Nodes
- Values of the Matrix represent the Maximum Weighted Edge in the Path b/w Row_Node & Col_Node
'''
from typing import List
from collections import defaultdict
class Solution:
    def maxEdgeSum(self, n : int, edges : List[List[int]]) -> int:
        # Making Adjacency List
        adjList = defaultdict(list)
        
        for edge in edges:
            u, v, w = edge[0], edge[1], edge[2]
            adjList[u].append( (v,w) )
            adjList[v].append( (u,w) ) # Undirected Graph
                
        maxWeightMatrix = [ [0] * (n+1) for _ in range(n+1) ]
        
        # DFS Function, which traverses from a Starting Node to all other Nodes(which are coming in Path)        
        def dfs(curNode, parent, startNode, curMaxWeight, adjList, maxWeightMatrix):
            '''
            Parameters:
            curNode : Current Node which is being Visited(Node that is being seen in Recursive call)
            parent : Parent Node,, as due to Recursive Calls we may re-visite the parent again,, at that time we need to stop
            startNode : Node from which we Originally started            
            curMaxWeight : Maximum Weight Until the Parent Node to Current Node
            adjList : Adjacency List
            maxWeightMatrix : Matrix which stores the Maximum Weighted Path b/w Parent Node & Current Node
            '''
            
            # Let's traverse the Nieghbours of Current Node
            for neighbours in adjList[curNode]:
                v = neighbours[0]
                w = neighbours[1]
                
                if v != parent: # Preventing the Re-Visit to Parent Node
                    newMaxWeight = max(curMaxWeight, w)
                    
                    maxWeightMatrix[startNode][v] = max(maxWeightMatrix[startNode][v], newMaxWeight)
                    # As Graph is Un-Directed,, we need to Update for both of the Nodes
                    maxWeightMatrix[v][startNode] = max(maxWeightMatrix[v][startNode], newMaxWeight) 
                    
                    # Recursive Call
                    dfs(v, curNode, startNode, newMaxWeight, adjList, maxWeightMatrix)
        
        # curMaxWeight = 0
        # We have to make a DFS for each Node(1 to n)
        for node in range(1, n+1):
            # Current Node & Start Node will be node
            # Let Parent be -1
            dfs(node, -1, node, 0, adjList, maxWeightMatrix)
            
        # Finding the Total Sum
        totalSum = 0
        for row in range(1, n+1):
            # As Graph is Un-directed &
            # Entries will be same for both Upper & Lower Triangle
            for col in range(row+1, n+1): # Considering Only Upper Triangle 
                totalSum = totalSum + maxWeightMatrix[row][col]

        return totalSum
