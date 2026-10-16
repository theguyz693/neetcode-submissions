class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       n=len(nums)
       res=[1]*(n)

       LeftOf_i=1
       for i in range(n):
         res[i]=LeftOf_i
         LeftOf_i *=nums[i] #so ure storing all products at each step till end.
       RightOf_i=1
       for i in range(n-1,-1,-1):#goes backward
         res[i]*=RightOf_i
         RightOf_i*=nums[i]
       return res