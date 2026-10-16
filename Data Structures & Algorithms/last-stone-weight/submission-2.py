class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       stones=[-s for s in stones]
       heapq.heapify(stones)

       while len(stones)>1:
         first= heapq.heappop(stones)
         second= heapq.heappop(stones)

         if second>first:
            heapq.heappush(stones,first-second)#second-first because both are negative terms and -ve second is greater than -ve first
       stones.append(0)
       return abs(stones[0])
