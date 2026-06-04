class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range (i+1, len(nums)):
                if i!=j:
                    if nums[i]+nums[j] == target:
                        listt= []
                        listt.append(i)
                        listt.append(j)
                        return listt
