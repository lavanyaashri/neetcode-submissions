class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = []
        seen2= []
        for i in s:
            seen.append(i)

        for j in t:
            seen2.append(j)
        seen.sort()
        seen2.sort()

        if seen == seen2:
            return True
        
        return False
