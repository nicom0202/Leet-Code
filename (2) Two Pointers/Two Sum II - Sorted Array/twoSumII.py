class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # two pointer approach front and back

        right = len(numbers) - 1
        left = 0
        result = []
        while left < right:

            # if numbers[right] + numbers[left] = target, return right and left
            if numbers[right] + numbers[left] == target:
                left += 1
                right += 1
                return [left, right]

            # if numbers[right] + numbers[left] > target, move left up (if left is 1 away from right move both up)
            if numbers[right] + numbers[left] > target:
                right -= 1
                continue

            # if numbers[right] + numbers[left] < target, move right up
            if numbers[right] + numbers[left] < target:
                left += 1
                continue

        return result