class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Idea: Bucket Sort with a twist. The index represents the occurance 
        #       and the value at that index will hold a list of ints with that occurance

        # Create a list of lists 
        occurance = [[] for _ in range(len(nums) + 1)]

        # Create a hash map
        hash_occurance = {}

        # iterate of nums, 
        for num in nums:
            # if num in hash_occurance, update occurance
            if num in hash_occurance:
                hash_occurance[num] += 1
            # if it doesn't exist, set it to 1
            else:
                hash_occurance[num] = 1

        # BIG IDEA: suppose nums is size 6, then there will be an occurance of at most 6 (aka the same num) therefore
        #           occurance is only going to be size 6, NOT the value of the elements

        # add all occurances of 1 to index 1, occurances of 2 to index 2, ..., occurances of n to index n
        for num in hash_occurance:
            occurance[hash_occurance[num]].append(num)

        # create a list called result that will hold the kth most frequent elements
        result = []

        # extract the last kth elements from occurance (aka the most frequent elements)
        for i in range(len(occurance) - 1, -1, -1):
            if k == 0:
                break
            result.extend(occurance[i])
            k -= len(occurance[i])

        return result
