def findWords(board,words):
    m=len(board)
    n=len(board[0])
    final=[]

    def backtrack(x,y,word,index):
        if board[x][y]!=word[index]:
            return False 
        if index==len(word)-1:
            return True 
        visited.add(x,y)
        index=index+1
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for dx,dy in directions:
            nx=x+dx 
            ny=y+dy 
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                if backtrack(nx,ny,word,index):
                    return True 
        visited.remove((x,y))
        return False
            

    for word in words:
        visited=set() #fresh start for each word
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and backtrack(i,j,word,0):
                    final.append(word)
    return list(set(final))

if you just return a list, it will append the same word multiple times if that word can be formed with different starting positions. so choose cast into a set, then a list and return the list

