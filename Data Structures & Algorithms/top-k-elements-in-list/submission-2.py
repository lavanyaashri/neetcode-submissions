class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        for i in nums:
            counts[i]=counts.get(i,0)+1
        
        pairs= list(counts.items())
        pairs.sort(key=lambda p:p[1], reverse=True)

        result=[]
        for i in range (k):
            result.append(pairs[i][0])
        return result
