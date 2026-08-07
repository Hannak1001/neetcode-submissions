class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}

        #add first word to hashmap
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        #subtract second word from hashmap
        for j in t:
            #if key doesn't exist or subtracting is less than 0, then invalid
            if j not in hashmap or hashmap[j] == 0:
                return False
            hashmap[j] -= 1
        return True
