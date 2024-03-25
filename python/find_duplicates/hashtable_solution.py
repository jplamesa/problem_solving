class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        keys = [None] * length

        for i in nums:
            if keys[i % length] is None:
                keys[i % length] = i 
            else:
                return i
