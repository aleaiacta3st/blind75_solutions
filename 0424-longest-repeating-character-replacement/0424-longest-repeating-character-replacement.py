class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result=0
        frequency={}
        left=0
        max_freq=0
        n=len(s)


        for right in range(n):
            frequency[s[right]] = frequency.get(s[right],0)+1
            max_freq=max(max_freq, frequency[s[right]])

            while (right-left+1) - max_freq > k:
                frequency[s[left]]-=1
                left=left+1
                

                max_freq=0
                for freq in frequency.values():
                    max_freq=max(max_freq,freq)


            result=max(result, right-left+1)


        return result

        