class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list=[[] for _ in range(numCourses)]
        in_degree_tracker = [0]*numCourses
        for course,prerequisite in prerequisites:
            adj_list[prerequisite].append(course)
            in_degree_tracker[course]+=1
        queue=deque()
        for course in range(numCourses):
            if in_degree_tracker[course]==0:
                queue.append(course)
        total_popped=0
        while queue:
            popped_prerequisite = queue.popleft()
            total_popped+=1
            for dependent in adj_list[popped_prerequisite]:
                in_degree_tracker[dependent]-=1
                if (in_degree_tracker[dependent]==0):
                    queue.append(dependent)
        return (total_popped==numCourses)

#this solves the course schedule problem thru kahn's algorithm
#topological sort by bfs
#why is this bfs?
    # You start with all nodes having in-degree = 0 — no dependencies.
    # Add them to a queue.
    # Repeatedly pop from the queue and process dependents.
    # Every time an in-degree hits zero, that node becomes ready and 
    # joins the queue.
    # You’re layering nodes level by level — exactly what BFS does.
    # The queue expands as new "ready" nodes are discovered, and you advance 
    # through them in breadth-first waves.
#Time complexity = O(V+E)
    # each action is accounted for only once.
    # You visit each vertex (V) exactly once when you add it to the queue or pop it out.
    # You visit each edge (E) exactly once when you reduce the in-degree of the dependent node.
    # At no point do you loop through all edges for every vertex (which would make it V * E).
    # Instead:
        # For each course (vertex), you only process its edges (dependencies) once.
        # Each edge is touched just one time — when it reduces the in-degree of a dependent.
        # Therefore, the work done is the sum of:
        # visiting every vertex + processing every edge

# Create an adjacency list. 
# The direction should be from prerequisites to its dependent courses.
# Create an in-degree array. 
# Fill this array up while you are building the adjacency list 
# Find nodes with in-degree 0. Push them into the queue.
# In-degree 0 means this is a subject which has no prerequisites. 
# Complete it. Completing means popping it out. 
# This popped out course must be acting as a preqrequisite for other courses.
# Once we have completed(popped out) this course, the burden on its dependent courses decreases. 
# For example, previously a course might have 3 prerequisites. After popping 1 course, it will now have only 2 prerequisites. 
# Check the adjacency list of the popped out course. 
# We have completed the popped out course. So decrease the burden on each of its dependents.
# If any of the dependent courses has now become free, ie its in-degree is 0, queue it up. 
# Every course popped is a course that has been completed.
# If the queue becomes empty, it means that there are no more courses which have 0 prerequisites.(in-degree=0)
# Now count the number of popped out courses. 
# If the total number of popped out courses is equal to the total number of courses, then a schedule exists 
# where all courses can be completed. Otherwise, a cycle exists and a course schedule is not possible.



        

    
