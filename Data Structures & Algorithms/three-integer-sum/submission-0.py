class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            target = -nums[i]

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[l] + nums[r]

                if total == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                elif total > target:
                    r -= 1

                else:
                    l += 1

        result = list(set(map(tuple,result))) # mapps all result lists as tuples, so we can put them in set to find distinct lists
        return result