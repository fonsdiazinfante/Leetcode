class Solution(object):
    def twoSum(self, nums, target):
        index = []
        for j in range(len(nums)):
            for i in range(len(nums)):
                if nums[j] + nums[i] == target and i != j:
                    index.extend([j,i])
                    return index
                else:
                    pass
        
