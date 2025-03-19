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
        