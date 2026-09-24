class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #value : key
        #number : index
        hashmap = {}
        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in hashmap:
                return [hashmap[partner], i]
            else:
                hashmap[nums[i]] = i
        return []
        