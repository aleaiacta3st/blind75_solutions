class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
    
        # Step 1: Transpose (swap across diagonal)
        for i in range(n):
            for j in range(i + 1, n):  # j > i to avoid double-swap
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()


# +-----+-----+-----+
# |  D  |  ↑  |  ↑  |   # i = 0
# +-----+-----+-----+
# |  ↓  |  D  |  ↑  |   # i = 1
# +-----+-----+-----+
# |  ↓  |  ↓  |  D  |   # i = 2
# +-----+-----+-----+

# # Legend:
# # D → Diagonal (i == j)
# # ↑ → Above Diagonal (i < j)
# # ↓ → Below Diagonal (i > j)


# why should j start from i+1
# If j were to start from 0 instead of i+1, we'd end up with the original matrix instead of a transposed one. Here's why:
# Each element pair across the diagonal would be swapped twice, effectively canceling out all our work.

# ou're absolutely right! Starting j from i instead of i+1 would work correctly, but it would include unnecessary operations.
# If j starts from i:

# You'd process the diagonal elements (where i=j)
# For these diagonal elements, you'd be swapping an element with itself
# This would be: matrix[i][i], matrix[i][i] = matrix[i][i], matrix[i][i]

# Simultaneous swap mechanics:
# a = 5
# b = 10

# If we want to swap their values, we typically need a temporary variable:
# temp = a  # temp = 5
# a = b     # a = 10
# b = temp  # b = 5

# But Python allows simultaneous swaps using the comma syntax:
# a, b = b, a

# Here's what happens behind the scenes:
# Python evaluates the right side b, a creating a tuple (10, 5)
# It unpacks this tuple into the variables on the left side
# a gets the first value (10)
# b gets the second value (5)


# The n//2 range parameter ensures you're only processing each element once - half the distance across each row is all you need when mirroring.

# why did transposing + mirror on the right side of the transposed matrix result in 90 degree clockwise rotation? what is the logic behind it?

        