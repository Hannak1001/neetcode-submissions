class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        #add number and their frequency to hashmap
        #number : frequency
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        #match frequency to bucket index
        bucket = [[] for x in range(len(nums)+1)]
        for key, value in freq.items():
            bucket[value].append(key)

        result = []
        #get top k values    
        for items in range(len(bucket)-1, -1, -1):
            #iterate through numbers with same frequency
            for i in bucket[items]:
                result.append(i)
                if k == len(result):
                    return result

