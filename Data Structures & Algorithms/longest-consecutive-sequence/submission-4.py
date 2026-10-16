class Solution:# normal sorting method not o(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        c=1
        i=0
        a=1
        while i<(len(nums)-1):
            if nums[i+1]==nums[i]:
                i+=1
                continue
            if nums[i+1]==nums[i]+1:
                c+=1
            if nums[i+1]!= nums[i] and nums[i+1]!=nums[i]+1:
                c=1
               
            a=max(c,a)            
            i+=1       
                
        return a