class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams={}
        n=len(strs)
        for i in range(n):
            if ''.join(sorted(strs[i])) in grouped_anagrams:
                grouped_anagrams[''.join(sorted(strs[i]))].append(strs[i])
            else:
                grouped_anagrams[''.join(sorted(strs[i]))] = [strs[i]]
        return list(grouped_anagrams.values())
        