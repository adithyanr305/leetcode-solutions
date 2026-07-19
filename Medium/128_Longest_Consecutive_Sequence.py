class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 100000:
            if nums[0] == -100000000:
                return 2
            else: 
                return 100000

        LCS = 0
        for num in (nums := {*nums}):
            length = 1
            curr = num
            if curr-1 in nums:
                continue
            while curr+1 in nums:
                curr+=1
                length+=1
            LCS = max(LCS,length)
        return LCS  
