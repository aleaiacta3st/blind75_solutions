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




# What's happening?
# You're doing DFS to perform a topological sort. That means you're trying to figure out:

# "What order should I put the letters in, so every letter comes before the ones it points to?"
# So let’s say you’re given:
# edges: a -> b, b -> c
# How DFS builds the list
# Start at 'a' → go to 'b' → go to 'c'
# 'c' has no neighbors → you add 'c' to your result
# Then you backtrack and add 'b'
# Then 'a'

# So your list becomes:
# ['c', 'b', 'a']

# Why reverse?
# Because the first letter you finish is the last one in the real order.
# So to get the correct topological order (where 'a' comes before 'b', and 'b' before 'c'),
# you must reverse the list at the end:
# ['a', 'b', 'c']

# tracker[subject] == 2
# It means:

# “We’ve already fully visited this course. We’ve explored all of its prerequisites. It’s done. It’s safe.”
# Why do we return True here?
# Because:
# You're in a DFS recursion.
# You've hit a node you've already completed in a previous DFS call.
# There’s no need to explore it again.
# It's confirmed to have no cycles.
# So, return True and save time. This is memoization in disguise — you’re saying:
# “I’ve seen this guy before. He’s not a problem. Move on.”

                
# what does rec func in course schedule do? it will take in a node and tell if there are any cycles in it while dfsing? is that it?
    

# The "app" and "apple" Issue in Alien Dictionary
# In a valid lexicographical ordering (whether English or alien):

# If a shorter word is a prefix of a longer word, the shorter word must come first
# For example, "app" should always come before "apple"

# The critical edge case in our alien dictionary problem occurs when:

# We find that two adjacent words share all characters up to the length of the shorter word
# Yet the longer word appears before the shorter word in the given list

# This represents an impossible ordering that violates fundamental dictionary principles. It would be like saying "apple" should come before "app" in English - which makes no logical sense in any consistent alphabet ordering.
# When we detect this scenario, we must return an empty string ("") to indicate that no valid alien alphabet exists, because the provided word ordering contains a contradiction.
# The solution requires carefully checking if we've reached the end of the shorter word without finding differences, then verifying if the longer word appears first - which signals an invalid dictionary.


# Alien Dictionary Algorithm Summary
# This algorithm solves the alien dictionary problem using topological sorting through DFS:

# Collects all unique letters from all words
# Builds a character dependency graph by comparing adjacent words
# Uses DFS with three states (0=unvisited, 1=in-progress, 2=completed) to detect cycles
# Returns a topologically sorted order of characters

# Common mistakes to watch for:

# Failing to handle the invalid case where a longer word comes before its prefix
# Incorrect cycle detection in DFS implementation
# Forgetting to reverse the result list at the end
# Not properly initializing the visited states for all characters
# Mishandling the comparison between adjacent words

# This is essentially a graph problem where characters are nodes and their relative ordering creates directed edges.


# this problem is very similar to the course schedule problem.
        