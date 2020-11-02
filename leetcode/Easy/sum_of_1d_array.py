class Solution(object):
    def runningSum(self, nums):
        i=[]
        j=0
        for x in range(len(nums)):
            j += nums[x] 
            i.append(j)
        return i
