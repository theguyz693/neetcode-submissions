class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])

        top,bot=0,row-1
        while top <=bot:
            xrow=(top+bot)//2
            if target> matrix[xrow][-1]:#right val lesser than target so move to next row
                top=xrow+1
            elif target < matrix[xrow][0]:
                bot=xrow -1
            else:
                break
        
        if not (top<=bot): return False

        xrow=(top+bot)//2
        l,r=0,col-1
        while l<=r:
            m=(l+r)//2
            if target > matrix[xrow][m]:
                l= m+1
            elif target < matrix[xrow][m]:
                r=m-1
            else :
                return True
        return False
            