class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #value : index
        hashmap = {}

        for i in range(len(nums)):
            targetPair = target - nums[i]
            if targetPair in hashmap:
                return[hashmap[targetPair], i]
            hashmap[nums[i]] = i
        return []
        