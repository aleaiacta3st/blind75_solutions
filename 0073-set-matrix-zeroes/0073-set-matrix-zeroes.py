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

        for i in range(1,m): #you don't want to zero the first row using markers you have in the first column. This is because the 0 in the first column can either be the original value or a marker that you have set.
        #assume there is a 0 in the first column. In your first pass, you set[0,0] to 0 because of this.
        #And assume there is no 0 in the first row originally
        #if you go by the marker, you will zero the first row which is wrong
            if matrix[i][0]==0: #markers in the first column used to zero rows except the first row
                for j in range(n):
                    matrix[i][j]=0 #rows being set to 0 except the first row

        for j in range(1,n):#similar logic
            if matrix[0][j]==0:#markers in first row used to zero columns
                for i in range(m):
                    matrix[i][j]=0 #columns being set to 0

        #innermatrix processed
        #observe that only first column and first have not been processed yet
        #You have to believe that every other column and row is processed because that is the truth
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

#we do not use the column markers to process the first row 
#we do not use row markers to process the first column

# what is the problem about?
# [
#   [1, 2, 3],
#   [4, 0, 6],
#   [7, 8, 9]
# ]
# Suppose you're scanning left to right, top to bottom. You hit matrix[1][1] == 0. You immediately zero its row and column:
# [
#   [1, 0, 3],  <-- You just zeroed this '2' to '0'!
#   [0, 0, 0],
#   [7, 0, 9]   <-- And this '8' too!
# ]
# Now, you continue scanning… then you hit matrix[0][1] == 0 (the one you just made). You think it was originally zero, but it wasn’t. You’ve now corrupted the truth.

# So you wrongly zero out all of row 0 and column 1 again. Now you set matrix[0][0] = 0 and matrix[0][2] = 0 — even though they were never meant to be touched.

# ❌ You’ve just wiped out innocent cells.