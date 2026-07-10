#15 ms:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
#5 ms:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        return len(nums) != len(unique)
#better solution is to create a set called unique and compare len of unique to len of nums array
