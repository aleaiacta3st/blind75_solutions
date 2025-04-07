class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        n=len(strs)
        for i in range(n):
            strs[i]=str(len(strs[i]))+'#'+strs[i]
        return "".join(strs)

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        collector=[]
        n=len(s)
        pointer=0
        while pointer<=n-1:
            temp=pointer
            while s[pointer].isdigit():
                pointer=pointer+1
            length=int(s[temp:pointer])
            collector.append(s[pointer+1:pointer+1+length])
            pointer=pointer+1+length
        return collector

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))