'''
Link : https://leetcode.com/problems/unique-paths-iii/description/

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
'''

'''
- At first we need to find the starting and target points
- From starting point to target point we have to find the parts as 4 directions
- He said that we have to cover all the non-obstacles means the cells which contain zero
- Let's also keep variable to store the total 0's in Matrix
'''
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        x_directions = [-1, 0, 1, 0]
        y_directions = [0, 1, 0, -1]

        def backtrack(grid, x, y, non_obstacles_until):
            '''
            (x,y) : Current Cell
            non_obstacles_until : Zeros saw until
            
            - For getting rid of re-visiting the same cells,, what we can do is we can use another visited data structure or we can mark the cell there itself
            - Ex: put -1
            '''
            # Base Case = Ans Checks + Boundary Checks
            if x < 0 or x >= num_rows or y < 0 or y >= num_cols or grid[x][y] == -1:
                return

            if grid[x][y] == 2:
                if non_obstacles_until == num_non_obstacles:
                    ans[0] += 1
                    return 

                elif non_obstacles_until < num_non_obstacles:
                    return  

            # Mark the cell from where you are checking neighbours
            grid[x][y] = -1
            for i in range(4):
                new_x = x + x_directions[i]
                new_y = y + y_directions[i]
                
                backtrack(grid, new_x, new_y, non_obstacles_until+1)

            grid[x][y] = 0

        
        # Main
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        starting_point = []
        ending_point = []
        num_non_obstacles = 0

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    starting_point.append(i)
                    starting_point.append(j)
                if grid[i][j] == 2: 
                    ending_point.append(i)
                    ending_point.append(j)
                if grid[i][j] == 0:
                    num_non_obstacles += 1
        
        # Starting point also in non obstacle
        num_non_obstacles += 1
        
        # Ending point is globally fixed so no need to pass as a parameter in backtrack function
        # Starting point is necessary because when we make the further recursive calls this the starting point of any changes
        non_obstacles_until = 0
        ans = [0]
        backtrack(grid, starting_point[0], starting_point[1], non_obstacles_until)

        return ans[0]
            
        
