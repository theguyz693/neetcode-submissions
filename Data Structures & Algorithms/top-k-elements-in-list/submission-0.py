class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq ={}
        

        for i in nums :
            freq[i]=freq.get(i,0)+1
        
        a=sorted(freq.items(), key=lambda x: x[1])[-k:]
        return [i[0] for i in a]
        # answer = []

        # for i in a:
        #     answer.append(i[0])

        # return answer