class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses 

        for course,prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course]=indegree[course]+1 

        queue=deque([i for i in range(numCourses) if indegree[i]==0])

        completed=0

        while queue:
            curr=queue.popleft()
            completed=completed+1
            for neighbor in adj[curr]:
                indegree[neighbor]=indegree[neighbor]-1
                if indegree[neighbor]==0:
                    queue.append(neighbor)


        return completed==numCourses
        