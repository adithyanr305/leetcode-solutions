class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        L = 0
        R = len(height) - 1
        while L<R:
            maximum = max(maximum,min(height[L],height[R]) * (R-L))
            if height[L] <= height[R]:
                prev = height[L]
                L+=1
                while L<R and height[L] <= prev:
                    L+=1
            else:
                prev = height[R]
                R-=1
                while L<R and height[R] <= prev:
                    R-=1
        return maximum
#easier solution
#def maxArea(self, height: List[int]) -> int:
#        maximum = 0
#        L = 0
#        R = len(height) - 1
#        while L<R:
#           maximum = max(maximum,min(height[L],height[R]) * (R-L))
#            if height[L] <= height[R]:
#                L+=1
#            else:
#                R-=1
#       return maximum
