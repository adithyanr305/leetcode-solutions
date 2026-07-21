class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        for i in range(len(nums)):
            mid = (right+left)//2
            if target < nums[mid]:
                right = mid-1
            elif target > nums[mid]:
                left = mid + 1
            elif nums[mid] == target:
                return mid
        return -1
