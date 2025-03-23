from collections import deque
def maxDepth(root):
    if not root:
        return 0
    queue=deque([root])
    depth=0
    while queue:
        k=len(queue)#gives the total nodes at a level
        for _ in range(k):
            n=queue.popleft()
            if (n.left):#add to queue only if the left child exists
                queue.append(n.left)
            if (n.right):#add to queue only if the right child exists
                queue.append(n.right)
        depth+=1
    return depth

# Count the number of levels
# BFS processes nodes level-wise 
# It means nodes in the left child and right child 
# at the same level are processed together
# The number of levels the BFS descends to is the total depth 

# For this,use the length of the queue
# increase depth only when all nodes at a level are processed
# at the first level - we have only 1 node(root)
# increase depth to 1 only after root has been popped

# The for loop is designed in such a way that at the start of every
# new while loop iteration the length of the queue contains exactly
# the total number of nodes at that level 
# So, now pop the queue exactly those many times to completely process
# that level and add its children

#         root
#        /    \
#      L1      R1
#     /  \    /  \
#   L2   R2  L3   R3
#
# Level 1: root
# Level 2: L1, R1
# Level 3: L2, R2, L3, R3
#
# BFS processes each level fully.
# The count of levels processed = max depth of tree.
