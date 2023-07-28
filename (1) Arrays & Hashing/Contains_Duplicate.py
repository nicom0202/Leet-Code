class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        elements = set()
        for i in range(len(nums)):
            if nums[i] in elements:
                return True
            elements.add(nums[i])

        return False
