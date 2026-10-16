class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=set(nums)
        if len(x)<len(nums):
            return True
        return False