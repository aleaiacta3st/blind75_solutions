class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for course,prereq in prerequisites:
            adj_list[course].append(prereq)
        tracker=[0]*numCourses
        def dfs(subject):
            if tracker[subject]==1:
                return False 
            if tracker[subject] == 2:
                return True
            tracker[subject]=1
            for prereq in adj_list[subject]:
                result = dfs(prereq)
                if result==False:
                    return False
            tracker[subject]=2
            return True
        for subject in range(numCourses):
            if not dfs(subject):
                return False
        return True


# In topological sorting, we need to list nodes so that all prerequisites come before
# their dependent courses. When a node "completes" in DFS, it means we've explored all'
# ' its descendants - which are precisely its prerequisites in a dependency graph.'

# for course,prereq in prerequisites
# That syntax is called "tuple unpacking" or "sequence unpacking" in a for loop.
# It's essentially the same as:
# for pair in prerequisites:
#     course = pair[0]
#     prereq = pair[1]
#     # do something 

# Make an adjacency list from the prerequisites list using the above syntax.
# Subjects are nodes, edges are prequisites 
# A cycle would make course scheduling impossible 
# Track 3 states for every subject
#     Untouched - 0
#     In progress - 1
#     Completed -2 

# You need to run DFS on every subject (course) because of one critical reason: 
# disconnected components in your graph.

# If topological sorting is possible, course scheduling is possible. 
# Otherwise, it's impossible.'
# ''
# this code wasnt trying to topologically sort them but was trying to detect cycles. 
# we do not know the actual topological sorting, but we do know there exists one because
# of the absence of cycles

# If you actually want the topological sort of the subjects:
#     DFS-based topo sort:
#         Do DFS on each node.
#         When DFS for a node finishes (i.e., after processing all children),
#         Add that node to a result list.
#         Reverse the result list at the end.    
#     BFS-based topo sort (Kahn’s Algorithm):
#         Start with all nodes having in-degree == 0.
#         Add them to a queue.
#         Pop one at a time, reducing in-degree of neighbors.
#         When new neighbors become in-degree == 0, push them in.
#         The order in which you pop is your topological order.

# for dfs based topo sort, which node do i start with? 
# will the final list be the same regardless of where i start?
#     You start with any unvisited node.
#     You pick any course that is still unvisited and run DFS.
#     Once its entire chain is explored, add it to your result list.
#     Repeat for all remaining unvisited nodes.

# Will the final order be the same regardless of where you start?
#     No, it does not have to be unique.
#     There can be multiple valid topological orders for the same graph.
#     Different DFS start points can produce different topological sorts.
#     But all valid topological sorts will respect the same global dependency constraints.
        