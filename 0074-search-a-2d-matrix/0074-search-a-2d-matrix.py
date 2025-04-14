class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        lo=0
        hi=m*n-1
        while lo<=hi:
            mid=(lo+hi)//2
            a=mid//n
            b=mid%n
            actual_mid=matrix[a][b]
            if target>actual_mid:
                lo=mid+1
            elif target<actual_mid:
                hi=mid-1
            else:
                return True 
        return False 


#the conditions of the problem are such that if the rows are placed one after the other, they would create a non decreasing sequence. Then do a binary search on the list you have created. 

"""
Search in a 2D Matrix - Binary Search Approach

Problem: Given an m x n matrix where each row is sorted in ascending order and 
the first element of each row is greater than the last element of the previous row,
search for a target value in the matrix.

Key Insight: Since the matrix has this special sorted property, we can treat it as a 
single sorted 1D array from indices 0 to m*n-1 and perform binary search.

Algorithm:
6. An element a,b in 2d will have index an+b in 1d
1. Calculate dimensions m (rows) and n (columns)
2. Treat the matrix as a virtual 1D array with indices from 0 to m*n-1
3. Perform standard binary search on this virtual array
4. Convert 1D indices to 2D coordinates using:
   - Row index (a) = mid // n (integer division by number of columns)
   - Column index (b) = mid % n (remainder when divided by number of columns)
5. Compare matrix[a][b] with target and adjust search bounds accordingly 

Time Complexity: O(log(m*n)) - Binary search on m*n elements
Space Complexity: O(1) - Only using constant extra space

This solution leverages row-major ordering (how 2D arrays are stored in memory)
to efficiently map between 1D indices and 2D coordinates.
"""
        