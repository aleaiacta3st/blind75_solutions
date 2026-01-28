class Solution:
    def firstUniqChar(self, s: str) -> int:


        answer_dict ={}

        n = len(s)

        for letter in s:
            answer_dict[letter] = answer_dict.get(letter,0)+1

        for i in range(n):
            if answer_dict[s[i]]==1:
                return i

        return -1

        