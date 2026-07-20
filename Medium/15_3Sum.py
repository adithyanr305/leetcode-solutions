class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for n in range(len(nums)):
            if nums[n] > 0:
                break
            if n > 0 and nums[n] == nums[n-1]:
                continue
            target = -nums[n]
            L = n+1
            R = len(nums)-1
            
            while L < R:
                if nums[L]+nums[R] > target:
                    R -= 1
                elif nums[L]+nums[R] < target:
                    L += 1
                else: 
                    result.append([nums[n],nums[L],nums[R]])
                    L+=1
                    R-=1
                    while L < R and nums[L] == nums[L-1]:
                        L+=1
                    while L<R and nums[R] == nums[R+1]:
                        R-=1
        return result
                    
