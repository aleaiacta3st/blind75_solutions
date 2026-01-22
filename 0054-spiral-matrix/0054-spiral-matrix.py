class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left=0
        right=len(matrix[0])-1

        top=0
        bottom = len(matrix)-1

        res=[]

        while left<=right and top<=bottom:

            for col in range(left,right+1):
                res.append(matrix[top][col])
            top=top+1

            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right=right-1

            if top<=bottom:
                for col in range(right,left-1,-1):
                    res.append(matrix[bottom][col])
                bottom=bottom-1

            if left<=right:
                for row in range(bottom,top-1,-1):
                    res.append(matrix[row][left])
                left=left+1


        return res

        