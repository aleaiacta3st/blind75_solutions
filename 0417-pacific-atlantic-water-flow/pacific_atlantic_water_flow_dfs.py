def pacificAtlantic(heights):
    m,n=len(heights),len(heights[0])
    can_reach_atlantic=set()
    can_reach_pacific=set()
    
    def dfs_atlantic(i,j):
        if (i,j) not in can_reach_atlantic:
            can_reach_atlantic.add((i,j))
            for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=a<m and 0<=b<n and heights[a][b]>=heights[i][j]:
                    dfs_atlantic(a,b)
    
    def dfs_pacific(i,j):
        if (i,j) not in can_reach_pacific:
            can_reach_pacific.add((i,j))
            for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=a<m and 0<=b<n and heights[a][b]>=heights[i][j]:
                    dfs_pacific(a,b)

    for j in range(n):
        dfs_atlantic(m-1,j)

    for i in range(m):
        dfs_atlantic(i,n-1)

    for i in range(m):
        dfs_pacific(i,0)

    for j in range(n):
        dfs_pacific(0,j)

    intersection_set = can_reach_pacific & can_reach_atlantic

    final_list=[]

    for i in intersection_set:
        final_list.append(list(i))

    return final_list
    


# python does not have a 2D matrix
# a list of lists mimcs as a 2D matrix 
# The bigger list which contains the smaller list is called the outer list 
# The inner lists are inner lists
# The first list is the first row 
# The second list is the second row and so on 
# That is why m = number of rows = len(heights). heights is a list 
# n = number of columns which is the length of any inner list, len(height[0])



# for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
#                 if 0<=a<m and 0<=b<n and heights[a][b]>=heights[i][j]:
#                     dfs(a,b)
# should you append (a,b) to visited immediately and 
# should you check if it has been visited previously?
# No. Once the recursive call dfs(a,b) is called,
# that would take care of adding/not adding to visited

# Difference between a set and a list:
# A set contains only unique immutable elements
# Tuples are immutable
# Lists are not 
# Sets have O(1) lookup and are efficient than lists
# So store the coordinates of the grid in tuple format 
# To add elements to a set the syntax is set_name.add(immutable_item)
# To create an empty set, empty_set=set()

# Start from the nodes bordering the oceans
# Treat each grid as a node 
# This is a connected graph
# If you deploy,dfs/bfs, all nodes can be reached from all nodes 
# But while visiting each node, we take care to add only those nodes which 
# make the flow of the water to the ocean bordering node possible
# So, choose only those nodes where height of that node>=height of ocean bordering node 
# This ensures flow of water in the direction of the ocean boredring node 

# Observe the unpacking syntax in the for loops

# A set has nodes which can reach the pacific 
# The other set has nodes which can reach the antarctic 
# Take the intersection of them 
# But this will be a set 
# Convert it into a list to get the desired answer