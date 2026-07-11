class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}                      # key: sorted word, value: list of words
        for word in strs:
            key = "".join(sorted(word))               # turn word into its sorted, hashable form
            if key not in groups:
                groups[key] = []
            groups[key].append(word  )         # put the ORIGINAL word into its pile
        return list(groups.values()  )       