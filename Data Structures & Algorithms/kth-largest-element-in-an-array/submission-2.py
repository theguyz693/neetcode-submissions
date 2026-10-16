class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[len(nums)-k]
        
       nums=[s for s in nums]
       heapq.heapify(nums)

       while len(nums)>k:
         heapq.heappop(nums)
       
       return (nums[0])