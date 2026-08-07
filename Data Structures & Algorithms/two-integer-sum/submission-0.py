class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #value : index
        hashmap = {} #previous values go in hashmap
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [hashmap[diff], index]
            hashmap[value] = index
                    