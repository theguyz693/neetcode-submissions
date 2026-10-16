class Solution:

    def encode(self, strs: List[str]) -> str:
        x=[]
        for i in strs:
            a=len(i)
            x.append(str(a)+"#"+i)
        return "".join(x)
        
    def decode(self, s: str) -> List[str]:
        y=[]
        i=0
        while i<len(s):
            j=s.find("#",i)
            length=int(s[i:j])
            word = s[j+1:j+1+length]
            i=j+1+length
            y.append(word)
        return y

