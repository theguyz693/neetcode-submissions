class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l,r=0,len(height)-1
        leftmax,rightmax = height[l],height[r]
        res=0
        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                res+=leftmax-height[l] #nothing to consider -ve values because we do max right before this so the rtesult will always be 0 or +ve.DF :( 
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                res+=rightmax-height[r]
        return res