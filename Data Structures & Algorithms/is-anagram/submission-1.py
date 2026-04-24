class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else: count[i] = 1
        for i in t:
            if i in count:
                count[i] -= 1
            else: count[i] = 1
        for val in count.values():
            if val != 0: return False
        return True