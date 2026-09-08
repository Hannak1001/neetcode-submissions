class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        #add first word to hashmap
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1

        #subtract second word from hashmap
        for l in t:
            if l not in hashmap or hashmap[l] == 0:
                return False
            hashmap[l] -= 1
        return True
        

