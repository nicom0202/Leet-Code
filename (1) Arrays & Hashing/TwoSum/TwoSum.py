class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a map called difference that holds each int's DIFFERENCE with target. key=difference : value=index  
        difference = {}

        # iterate over nums
        for i in range(len(nums)):
            # check if difference contains a previous answer needed
            if target - nums[i] in difference:
                result = []
                result.append(difference[target-nums[i]])
                result.append(i)
                return result
            # add to difference
            difference[nums[i]] = i