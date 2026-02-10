class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        frequency={}
        for task in tasks:
            frequency[task]=frequency.get(task,0)+1
        
        heap=[]
        for task,freq in frequency.items():
            heapq.heappush(heap,-freq)


        cooldown=deque()

        time=0

        while heap or cooldown:
            time+=1
            if heap:
                freq=-heapq.heappop(heap)
                if freq-1>0:
                    cooldown.append((time+n,freq-1))
            if cooldown and cooldown[0][0]==time:
                heapq.heappush(heap,-cooldown.popleft()[1])


        return time


        