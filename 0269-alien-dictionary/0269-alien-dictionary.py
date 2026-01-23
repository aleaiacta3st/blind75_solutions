class Solution:
    def alienOrder(self, words: List[str]) -> str:

        adj={}


        for word in words:
            for letter in word:
                if letter not in adj:
                    adj[letter]=set()



        indegree={letter:0 for letter in adj.keys()}


        n=len(words)

        for i in range(n-1):
            min_len=min(len(words[i]),len(words[i+1]))

            if len(words[i]) >len(words[i+1]):
                if words[i][:min_len] == words[i+1][:min_len]:
                    return ""

            for j in range(min_len):
                if words[i][j] != words[i+1][j]:
                    if words[i+1][j] not in adj[words[i][j]]:
                        adj[words[i][j]].add(words[i+1][j])
                        indegree[words[i+1][j]]+=1
                    break


        queue=deque([char for char in indegree if indegree[char]==0])
        res=[]

        while queue:
            letter_popped = queue.popleft()
            res.append(letter_popped)
            for neighbor in adj[letter_popped]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)


        return ''.join(res) if len(res)==len(adj) else ""

        