class LRUCache:
    class Node:
        def __init__(self, key,value,prev=None,next=None):
            self.value=value
            self.prev=prev
            self.next=next
            self.key=key

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            node.prev.next=node.next
            node.next.prev=node.prev
            head_next=self.head.next
            self.head.next=node
            node.next=head_next
            head_next.prev=node
            node.prev=self.head
            return node.value
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            node.prev.next=node.next
            node.next.prev=node.prev
            head_next=self.head.next
            self.head.next=node
            node.next=head_next
            head_next.prev=node
            node.prev=self.head

        else:
            if len(self.cache)<self.capacity:
                node = self.Node(key, value) #create a node
                self.cache[key]=node #make an entry in the dictionary
                head_next=self.head.next 
                self.head.next=node 
                node.next=head_next 
                node.prev=self.head 
                head_next.prev=node
            else:
                del self.cache[self.tail.prev.key]
                node = self.Node(key, value) #create a node
                self.cache[key]=node #make an entry in the dictionary
                self.tail.prev.prev.next=self.tail
                self.tail.prev = self.tail.prev.prev
                head_next=self.head.next 
                self.head.next=node 
                node.next=head_next 
                node.prev=self.head 
                head_next.prev=node







# LRU Cache(dictionary) matches key to a node.
# LRU CACHE: ALGORITHM AND LOGIC
# Here's a comprehensive explanation of your LRU (Least Recently Used) Cache implementation:
# Core Concept
# The LRU Cache maintains a fixed-size collection of key-value pairs, automatically evicting the least recently accessed item when capacity is reached. This mimics how computer memory systems prioritize recently accessed data.
# Data Structures
# Your implementation uses two synchronized data structures:

# Hash Map (Dictionary): Provides O(1) key lookups
# Doubly-Linked List: Tracks access order with O(1) node repositioning

# Key Components

# Node Class: Stores key, value, and maintains prev/next pointers
# Sentinel Nodes: Head and tail dummy nodes simplify edge cases
# Cache Dictionary: Maps keys to Node objects for direct access

# Operations Logic
# GET Operation

# Check if key exists in cache
# If missing: Return -1
# If found:

# Remove node from current position
# Move node to front (most recently used position)
# Return the value



# PUT Operation

# Check if key already exists:

# If exists: Update value and move to front
# If new:

# If under capacity: Create node, add to front, register in cache
# If at capacity: Remove least recently used node (tail.prev), add new node to front





# Time Complexity

# Get: O(1) lookup and repositioning
# Put: O(1) for all operations

# Memory Usage

# O(capacity) for both the dictionary and linked list structures

# This implementation balances rapid access with intelligent memory management, making it ideal for caching systems where recency of use predicts future access patterns.

# node = self.Node(key, value)

# explain why during creation we use self. but subsequently we dont. speak like you normally do without a voice. i did not ask for a hint.
# The difference between using self.Node(key, value) during creation and not using self afterward relates to how Python handles nested classes.
# When you create a new Node with node = self.Node(key, value), you're accessing the Node class definition that lives inside the LRUCache class. The self here is required because you're accessing something that belongs to the LRUCache instance - specifically, its nested Node class.
# Think of it this way: The Node class is defined inside LRUCache, so it's like a blueprint that belongs to LRUCache. To access this blueprint and create a Node, you need to go through the LRUCache instance (which is what self refers to in LRUCache methods).
# Once you've created a Node instance and stored it in the node variable, you're now dealing with that specific Node object directly. The variable node now holds a reference to a Node instance, not to something that belongs to the LRUCache instance. Therefore, you access its properties directly with node.value, node.next, etc.
# This is standard Python object-oriented programming - you use self to access attributes and methods that belong to the current instance, but once you have a separate object stored in a variable, you access that object's attributes directly through the variable name.