class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            sortedWord = ''.join(sorted(i))
            hashmap[sortedWord].append(i)
        return list(hashmap.values())