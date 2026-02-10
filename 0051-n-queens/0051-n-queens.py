class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col=set()
        row_plus_col=set()
        row_minus_col=set() 

        board=[['.']*n for _ in range(n)]

        result=[]




        def backtrack(row):
            if row==n:
                result.append(["".join(row) for row in board])
                return
            for j in range(n):
                if j not in col and (row+j) not in row_plus_col and (row-j) not in row_minus_col:
                    board[row][j]='Q'
                    col.add(j)
                    row_plus_col.add(row+j)
                    row_minus_col.add(row-j)
                    backtrack(row+1)
                    board[row][j]='.'
                    col.remove(j)
                    row_plus_col.remove(row+j)
                    row_minus_col.remove(row-j) 


        backtrack(0)

        return result



                









        