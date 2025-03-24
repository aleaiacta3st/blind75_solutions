def levelOrder(root):
    if not root:
        return [] 
    level_order_traversal_list=[]
    def dfs(root,level):
        if root==None:
            return root
        if level==len(level_order_traversal_list):
            level_order_traversal_list.append([])
        level_order_traversal_list[level].append(root.val)
        dfs(root.left,level+1)
        dfs(root.right,level+1)
    dfs(root,0)
    return level_order_traversal_list
        

# when you enter an element of level i for the first time, there is no 
# empty list which is an element of the traversal list 
# so create that first and then add your node to it

# in graphs, while doing dfs, i used to write a for loop for 
# all neighbors in neighbor list and then called dfs on them but
# in trees i am doing it consecutively why? is it because there are just 
# 2 children
# In graphs, you need a systematic way to visit all neighbors 
# from an adjacency list, which could be any number... 
# but in binary trees, you're dealing with a fixed structure '
# 'where each node has at most two specific children - left and right.'

# in graphs:
# Each node can have any number of neighbors
# Neighbors are typically stored in an adjacency list
# You need a loop to iterate through all possible neighbors
# You often need a "visited" set to avoid cycles

# In binary trees:
# Each node has at most 2 children (left and right)
# These children are specific properties of the node
# You can directly access them by name (node.left, node.right)
# Trees are acyclic by definition, so no "visited" set needed

# what is the base condition for my recursive function
# if root is None:
#     return
# If the current node is missing (null), there’s nothing left to 
# process — so stop and return.

# so i go to a leaf and then call dfs on its non existent nodes, i return
# The recursion will go down the tree until it reaches a leaf.
# At the leaf:
# It will attempt dfs(left_child_of_leaf) and dfs(right_child_of_leaf).
# Both calls find root is None.
# Condition met. Termination signal triggered. Return.
# It is safe. It is efficient. The recursion then unwinds — mission complete.
# You terminate only when the tree’s structure ends.

# the contro returns to dfs(leaf)?
# When you call:
# dfs(leaf)
# inside that function:
# It processes leaf by adding its value to level_order_traversal_list.
# Then it calls:
# dfs(leaf.left)  
# dfs(leaf.right)
# Both leaf.left and leaf.right are None.
# At those calls, it hits the base condition:
# if root is None:
#     return
# The control flow returns step-by-step:
# from dfs(None) → back to dfs(leaf), finishes;
# from dfs(leaf) → back to its parent call;
# and so on, up the call stack.
# No values are returned; control simply unwinds.
# ok. so the nodes are in the traversal list as soon as we call the dfs 
# function on them, but the function calls are stuck in the stack until 
# the call above them finishes.











