class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        if len(s)!= len(t):
            return False
        
        for i in s:
            freq[i]= freq.get(i,0)+1
        for i in t:
            freq[i]= freq.get(i,0)-1
        for i in freq.values():
            if i!=0:
                return False
        return True
        

