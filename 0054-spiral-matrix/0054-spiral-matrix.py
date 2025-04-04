class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_list=[]
        m=len(matrix)
        n=len(matrix[0])

        top=0
        bottom=m-1
        left=0
        right=n-1

        while (top<=bottom) and (left<=right):
            for j in range(left,right+1): #left to right, row processed
                spiral_list.append(matrix[top][j])

            for i in range(top+1,bottom+1): #on right: top to bottom, col processed
                spiral_list.append(matrix[i][right])

            if not top==bottom:
                for j in range(right-1,left-1,-1):#right to left, row processed
                    spiral_list.append(matrix[bottom][j])

            if not left==right:
                for i in range(bottom-1,top,-1):#bottom to top, column processed
                    spiral_list.append(matrix[i][left])

            top+=1
            bottom-=1
            left+=1
            right-=1

        return spiral_list


# while (top<=bottom) and (left<=right)
# if it is just t<b and l<r, you will miss one row and one column. These are the final passes. 

# In Python, the range() function works on the principle of "inclusive start, exclusive end":
# range(start, stop, step)
# When start equals stop, the range produces no values because:

# The function starts at the start value
# It continues generating values until it reaches the stop value (which is not included)
# If start already equals stop, the stopping condition is immediately met, so no values are generated

# so range(x,x) does not generate any values 



# top < bottom works for matrices with even rows. top will never be equal to bottom. and the state jumps directly from top<bottom to top > bottom. 
# we need not worry about top=bottom and values being duplicated because top=bottom is an impossibility in matrices with even number of rows.

# but for matrices with odd number of rows. we need to allow for top=bottom. the final row which needs to be processed. the state jumps from top<bottom to top=bottom to top>bottom. top>bottom needs to be avoided because it results double processing.
    
# if top equals bottom, you have but a single row! If you process it with both your first AND third loops, you count the same elements twice! Similarly, if left equals right, a single column would be processed by both second AND fourth loops!"

# therefore when top equals to bottom disable the third loop to prevent double counting

# when left=right, disable the fourth loop to prevent double counting

# range with negative steps.(3rd and 4th loops) watch out. 
# # This generates: 5, 4, 3, 2 (but NOT 1)
# list(range(5, 1, -1))  

# # This generates: 5, 4, 3, 2, 1 (stops before reaching 0)
# list(range(5, 0, -1))

# left-2 left-1 left left+1 left+2          right 
# if you are starting from right and want left to be included the stop value should be left-1
        