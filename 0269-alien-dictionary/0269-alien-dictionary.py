class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n=len(words)
        result=[]
        
        collector_of_letters_in_alien_words=set()
        for word in words:
            for letter in word:
                collector_of_letters_in_alien_words.add(letter)

        
        adj_list={letter: [] for letter in collector_of_letters_in_alien_words}
        for i in range(n-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j]!=words[i+1][j]:
                    adj_list[words[i][j]].append(words[i+1][j])
                    break
                else:
                    if j + 1 == len(words[i+1]) and len(words[i])>len(words[i+1]):#these are the cases where apple comes before app
                        return ""
                    
        visited={}
        for letter in collector_of_letters_in_alien_words:
            if letter not in visited:
                visited[letter]=0

        def dfs(letter):
            if visited[letter]==1:
                return False
            if visited[letter]==2:
                return True 
            visited[letter]=1
            for neighbor in adj_list[letter]:
                if not dfs(neighbor):
                    return False
            visited[letter]=2
            result.append(letter)
            return True

        for letter in collector_of_letters_in_alien_words:
            if not dfs(letter):
                return ""

        result.reverse()

        string_result=''.join(result)

        return string_result
        