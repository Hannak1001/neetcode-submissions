class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #value : index
        hashmap = {}
        for index, number in enumerate(nums):
            targetPair = target - number
            if targetPair in hashmap:
                return [hashmap[targetPair], index]
            hashmap[number] = index
        