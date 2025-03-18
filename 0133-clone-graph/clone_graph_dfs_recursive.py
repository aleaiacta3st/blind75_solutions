def cloneGraph(node):
    if not node:
        return None
    cloned={}
    def deepClonedfs(original):
        if original in cloned:
            return cloned[original]
        cloned[original]=Node(original.val)
        cloned[original].neighbors=[]
        for neighbor in original.neighbors:
            cloned[original].neighbors.append(deepClonedfsdfs(neighbor))
        return cloned[original]
    return deepClonefs(node)




#the dfs that is used here is not just for searching. 
# we augment it to even clone the nodes.

#the dfs(neighbor) call returns a clone of the neighbor



#Consider the graph A>B>C>A
#There is a loop from C to A
#Call dfs(A)
#that calls dfs(B) which calls dfs(C) which again calls dfs(A)
#this cycle of recursion will never end
#this is where the dictionary comes into play
#The first time we encounter a node, we create a new copy of it,
#  store it in cloned, and start filling its neighbors. 
# If we ever encounter the same node again later in the recursion, 
# we don't repeat the cloning process—we simply return the 
# existing clone immediately.
#A for loop in Python only runs if there is something to 
# iterate over. If the collection is empty, the loop body is 
# completely skipped.

# Observe that we are finally returning a single node.
# So, how can leetcode check if all the other edges and nodes are cloned as expected?
# We return cloned[original]
# In memory it exists like cloned[original.val] and [clonednode2,clonednode3]
# clonednode2 and clonode3 are node objects and they have their own neighbors
# so by returning a reference to a single node, leetcode will be able to traverse 
# the entire graph.

#The neighbor list of cloned[original] is built last because of 
# recursion’s Last-In-First-Out (LIFO) nature
#When we do DFS recursion, each function call waits until all its recursive calls 
# finish before adding neighbors. This means:
    # The first node we start cloning is the last one to finish setting up its neighbors.
    # The deepest node in the recursion tree (the last one to be visited) finishes first.

#  1 -- 2 -- 3
#Calling dfs(1) starts the cloning process:
    # dfs(1) calls dfs(2) before finishing.
    # dfs(2) calls dfs(3) before finishing.
    # dfs(3) has no new neighbors left, so it returns first.
    # dfs(2) can now add dfs(3)'s result to its neighbors and return.
    # dfs(1) can now add dfs(2)'s result to its neighbors and return.
# Since dfs(1) was the first function called, it is the 
# last function to complete, and its neighbors list is the last to be fully built.

#Creation order is pre-order, going down the recursion.
    #Node1, Node2,Node3
#Connection order is post-order, as recursion unwinds
    #Complete cloned[node3].neighbors first
    # Then cloned[node2].neighbors
    # Finally cloned[node1].neighbors

#1️First Thought: "DFS(node) Should Return a Clone"
# Before even thinking about memoization (cloned dictionary), 
# the key insight is:
# "What should dfs(node) return?"
# Since we want to recreate the graph, we expect dfs(node) to 
# return a clone of node.
# If dfs(node) properly returns a clone, then recursively calling 
# dfs(neighbor) will return cloned neighbors.
# this naturally leads to dfs(node) → returns a clone of `node`

# Second Thought: "How Do We Prevent Infinite Recursion?"
# If the graph has cycles, a naive DFS could run forever.
# If a node has already been cloned, we shouldn’t recreate 
# it—we should return the existing clone.
# This leads to the need for a way to remember already-cloned nodes.

# Third Thought: "We Need a Dictionary for Memoization"
# To avoid cloning the same node multiple times, we need a 
# dictionary (cloned).
# The dictionary will map original nodes to their clones, 
# so we don’t reprocess them.








