class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()

        q=[]

        for index,value in enumerate(queries):
            q.append((value,index))

        q.sort()

        heap=[] 

        n=len(queries)

        m=len(intervals)

        res=[-1]*n

        j=0

        for i in range(n):
            while j<m and intervals[j][0]<=q[i][0]:
                heapq.heappush(heap,(intervals[j][1]-intervals[j][0]+1,intervals[j][1]))
                j=j+1
            while heap and heap[0][1]<q[i][0]:
                heapq.heappop(heap)
            if heap:
                res[q[i][1]]=heap[0][0]


        return res
            



                    


                