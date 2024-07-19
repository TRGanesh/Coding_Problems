'''
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
'''

'''
- Let's the store minimum guy for each row and maximum guy for each column
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        row_min = []
        col_max = []
        
        for i in range(num_rows):
            row = matrix[i]
            # Append Row Min in the LIst
            row_min.append( min(row) )
        
        for col in range(num_cols):
            col_maxi = float('-inf')
            for row in range(num_rows):
                col_maxi = max(col_maxi, matrix[row][col])
            
            col_max.append(col_maxi)

        print(row_min)
        print(col_max)

        ans = []
        for i in range(num_rows):
            for j in range(num_cols):
                ele = matrix[i][j]
                if ele == row_min[i] and ele == col_max[j]:
                    ans.append(ele)

        return ans
