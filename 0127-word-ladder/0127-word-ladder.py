class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set=set(wordList)

        visited=set([beginWord])

        queue=deque([(beginWord,1)])

        while queue:
            word,distance=queue.popleft()
            n=len(word)
            for i in range(n):
                for ch2 in 'abcdefghijklmnopqrstuvwxyz':
                    new_word=word[0:i]+ch2+word[i+1:]
                    if new_word==endWord and endWord in word_set:
                        return distance+1
                    if  new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word,distance+1))

        return 0






        