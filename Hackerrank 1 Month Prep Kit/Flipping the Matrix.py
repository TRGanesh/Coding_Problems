'''
You are given a 2n x 2n matrix (a square matrix with even dimensions). 
You are allowed to flip any of its rows or columns. 
The goal is to maximize the sum of the elements in the upper-left quadrant of size n x n.
'''

'''
- There Will be four parts for a n x n Matrix. 
   - Upper-Left, Upper-Right, Lower-Left, and Lower-Right
- Soo,, We want to Maximise the Upper-Left part
- Okayy,, We can Reverse the Row or Column
- We have to compare Upper-Left part elements with corresponding elements in other Quadrants
- Dimensions of Matrix are Even(2n)
- We have to Find the Range(of Row_Number & Col_Number),, where Upper-Left part exists
- Row_Number Range --> [0, n], Col_Number Range --> [0, n]
'''
def flippingMatrix(matrix):
    n = len(matrix) // 2
    
    ans = 0
    for row_num in range(0, n):
        for col_num in range(0, n):
            
            cur_ele = matrix[row_num][col_num]
            
            # Row Comparision in Complementary Quadrants
            complement_row_ele = matrix[row_num][(2*n - (col_num+1))]
            
            # Col Comparision in Complementary Quadrants
            complement_col_ele = matrix[(2*n - (row_num+1))][col_num ]
            
            other_ele = matrix[2*n - (row_num+1)][2*n - (col_num+1)]
            
            print('Ele', matrix[row_num][col_num])
            print('Complement Row Ele', complement_row_ele)
            print('Complement Col Ele', complement_col_ele)
            print('Other Ele', other_ele)
        
            ans += max(cur_ele, complement_row_ele, complement_col_ele,other_ele)
            print('maxi ',max(cur_ele, complement_row_ele, complement_col_ele,other_ele))
    return ans
