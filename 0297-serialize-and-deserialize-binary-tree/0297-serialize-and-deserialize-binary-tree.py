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