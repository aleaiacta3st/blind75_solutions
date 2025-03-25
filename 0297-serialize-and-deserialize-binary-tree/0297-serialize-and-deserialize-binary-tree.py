# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        serialized=[]
        queue=deque([root])
        while queue:
            n=len(queue)
            for i in range(n):
                popped_node=queue.popleft()
                if popped_node!=None:
                    serialized.append(str(popped_node.val))
                    queue.append(popped_node.left)
                    queue.append(popped_node.right)
                else:
                    serialized.append("null")
        return "[" + ",".join(serialized) + "]"
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data or data == "[]":
            return None
        data = data[1:-1].split(",")
        root = TreeNode(int(data[0]))
        parents_that_need_children_assigned=deque([root])
        data_walker=0
        while parents_that_need_children_assigned and data_walker<len(data):
            popped_parent=parents_that_need_children_assigned.popleft()
            if popped_parent is not None:
                if data_walker+1<len(data) and data[data_walker+1]!="null":
                    popped_parent.left = TreeNode(data[data_walker+1])
                    parents_that_need_children_assigned.append(popped_parent.left)
                if data_walker+2<len(data) and data[data_walker+2]!="null":
                    popped_parent.right = TreeNode(data[data_walker+2])
                    parents_that_need_children_assigned.append(popped_parent.right)
            data_walker+=2
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Serialize:
# Similar to level order traversal
# But here we want to include None as well 

# Deserialise:
# Create the root node from the first element of data 
# Create a queue which tracks the parents who need to have children assigned
# Pop from the queue 
# Assign children to it from data 
# Now children nodes are created 
# But they are not yet assigned children of their own yet 
# Queue them up 

# Additionally we also need to have a tracker which tracks which element in 
# the data list we are at.


# it is not that children are in the next two position of the popped node, 
# but the next 2 unassigned children are assigned to it.
# Exactly. In a BFS serialization, the parent’s own index in the data array 
# isn’t what determines where its children appear. Instead, there's a single '
# '"child pointer" or index that’s always advancing to the next unprocessed '
# 'child entries. Each parent, in the order it’s dequeued, receives the next '
# 'two unclaimed child entries from that pointer. Once assigned, the pointer '
# 'jumps past those two entries, ready for the next parent. So while it feels '
# 'like “popped node at index X has children at indices X+1 and X+2,” in '
# 'reality it’s “popped parent gets whatever two child spots come next '
# 'in the queue.”'

# if data[data_walker+1]
# if this is the only check, 0 in python is falsey. 
# so if the child’s value is actually zero, it won’t create that node. 
# The usual fix is to check for None rather than relying on truthiness:
# if data[data_walker + 1] is not None:


# The queue and data appear to be in sync but they may not be. 
# The queue may have parents with unassigned children while we have exhausted 
# the children that can be assigned in data. 
# So only while parents_that_need_children_assigned: is not enough 
# we need to have while queue and i < len(data):
# so that we stop looping when we hit the end of data 
# whatever nodes remaining in the queue are leaves 

# at the start of while loop, we did an index check,
# while processing each of the children also, we did an index check 
# isnt the first condition alone sufficient?
# no 
# the first check checks for i 
# it does not check for i+1 and i+2 inside the while loop also staying 
# within bounds 
# that is why both checks are necessary 

# Each BFS round: You pop one parent from the queue. 
# In an ideal world, you then read two child values from data 
# (one for the left child, one for the right). If they exist, 
# you attach them to the parent and enqueue those children.

# Truncation scenario: Now imagine the data does not have enough child entries 
# left to match the number of parents that remain in the queue. You’ll reach a 
# point where there are still nodes in the queue (each awaiting children), 
# but you’ve used up all your serialized data. If your code tries to read 
# another child from data at this point, it goes beyond the valid indices 
# and triggers an IndexError.

# The while i < len(data) check ensures you never enter the loop if you’ve 
# run out of data. Meanwhile, the individual checks inside the loop 
# protect against situations where you might do something like 
# data[i + 1] or data[i + 2] if you’re near the boundary. 
# Relying solely on try/except blocks or only checking inside the 
# loop can still let you into a situation where the loop itself is 
# active, but no valid data remains to process.

#  What is null vs. "null"?
# null (without quotes) doesn’t exist in Python.
# In Python, we use None.
# But in string output (like serialize() return), you must return a string. 
# You cannot return a Python object like None.
# So we represent None in the output by the string "null". 
# This is a LeetCode convention.
# ⚔️ Bottom line:
# Inside Python: None
# In output string: "null"

# What is ""?
# An empty string.
# If the tree is empty, we initially tried returning "". But LeetCode wants "[]" (an empty list in string form).
# So if root is None, you must return "[]" instead of "".
# ⚔️ Bottom line:
# Empty tree output: "[]" not "".

# 3️⃣ Why do we join by commas?
# Your serialized data needs to look like:
# [1,2,3,null,null,4,5]
# This means after converting every node or None into strings, 
# you join them with commas using:
# ",".join(serialized)

# 4️⃣ Why wrap it in brackets?
# eetCode doesn’t want just 1,2,3,null,null,4,5 — it wants:
# [1,2,3,null,null,4,5]
# So we put square brackets around that string using:
# "[" + ",".join(serialized) + "]"

# 5️⃣ During deserialization, what do we do with brackets?
# ou receive something like:
# "[1,2,3,null,null,4,5]"
# You cannot split this directly — it includes brackets.
# So you remove the first and last character:
# data = data[1:-1].split(",")
# This leaves you with: ["1", "2", "3", "null", "null", "4", "5"]
# And then you turn each "null" back into None in logic, or skip creating 
# children if it’s "null".

# What did you return in Level Order Traversal problem?
# In that problem, you:
# Traverse the tree level by level.
# Storethe val of each node in a list of lists (each inner list for one level).
# Finally, return a list of lists like:
# ➡️ You returned a Python data structure (list of lists).

# 2️⃣ What are we returning in serialize?
# LeetCode asks you to store the tree structure in a string form, 
# so that it can be easily transmitted/stored.
# Instead of returning a Python list or object,
# You flatten the tree level order into a list with None represented by "null",
# Then convert this whole list into a single string that looks like a list:
# "[1,2,3,null,null,4,5]"
# You are not just returning values. You’re returning a blueprint of the tree in string form.

# 3️⃣ Why return a string in serialize()?
# Imagine this as "saving" the tree.
# Python lists are Python objects — can’t easily transmit or store outside Python.
# Strings can be stored in databases, sent over networks, saved in files.
# The string has to contain all the structure (with nulls), not just values.
# That’s why serialize() returns a single string

# serialize() = "Save this tree into a string blueprint."
# deserialize() = "Take that blueprint string and rebuild the actual tree."

# Operation	Input	              Output
# Level Order	Tree	               List of lists (each list is values at one level)
# Serialize	Tree	                A single string that looks like a flattened tree: "[1,2,3,null,null,4,5]"
# Deserialize	That string blueprint	Reconstructed tree (root node of type TreeNode)

""" 
when you do level order traversal and serialize the tree in the list data
what you get is root followed by sets of children
it looks like
data = [root children children children .....]
consider the tree 
        0
      /   \
     1     2
    / \   / \
   3   4 5   6
when you serialize using level order traversal
data = [0 1 2 3 4 5 6]
data = [[root] [children of 0] [children of 1] [children of 2]]
for every node popped out of queue you just assign the next children set in data
that is why data_walker+1 and data_walker+2 might make this misleading
you are just assigning the next children set to the popped parent
better approach is 
i=0
assign left child
i+=1
assign right child
i+=1
an additional advantage of this style is that you don't have to check 
if i+1 and i+2 are in range, just do one check for i at the while loop and that
would be sufficient
"""

# When using level-order (BFS) serialization, what we're creating is essentially
#  a flattened representation of the tree by levels:
# [root, level1_node1, level1_node2, level2_node1, level2_node2, level2_node3, 
# level2_node4, ...]
