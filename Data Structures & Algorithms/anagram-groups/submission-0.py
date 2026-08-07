class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            sortedWord = tuple(sorted(i))
            if sortedWord not in hashmap:
                hashmap[sortedWord] = []
            hashmap[sortedWord].append(i)
        return list(hashmap.values())