class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])

        first_row_has_0=False 
        first_column_has_0=False


        for j in range(n):
            if matrix[0][j]==0:
                first_row_has_0=True
                break

        for i in range(m):
            if matrix[i][0]==0:
                first_column_has_0=True
                break

        for i in range(m): #markers stored in first row and first column
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0 

        for i in range(1,m): #leave first row for now. The 0 at that location might have been its original inhabitant or it might have been set by you. Consider an original 0 below the first row. This introduces a 0 in the first row. So if you consider that as original 0, you would nuke that entire row when you shouldn't.
            if matrix[i][0]==0: #markers in the first column used to zero rows
                for j in range(n):
                    matrix[i][j]=0 #rows being set to 0

        for j in range(1,n):#similar logic
            if matrix[0][j]==0:#markers in first row used to zero columns
                for i in range(m):
                    matrix[i][j]=0 #columns being set to 0

        #innermatrix processed
        #now deal with first row and first column

        if first_row_has_0:
            for j in range(n):
                matrix[0][j]=0

        if first_column_has_0:
            for i in range(m):
                matrix[i][0]=0 



# The question is we have set the first row or first column to zero depending on the boolean flag. but what about their associated rows and columns?
# They are set to while we are processing the inner matrix. 
# Consider a 0 at [0][1]
# we set 
# mat[0][0]=0 
# mat[0][1]=0
# so the first column needs to be set to 0
# This inner processing block does exactly that
#     for j in range(1,n):#similar logic
#         if matrix[0][j]==0:#markers in first row used to zero columns
#             for i in range(m):
#                 matrix[i][j]=0 #columns being set to 0
        

# The elegant part is that the order of operations matters:
# First we mark which rows/columns need zeroing (using first row/column)
# Then we process rows first (based on first column markers)
# Then we process columns (based on first row markers)
# Finally, we handle the first row and column using our boolean flags