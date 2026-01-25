class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = {}
        ans = []
        for i in range(len(nums)):
            x = target - nums[i]

            if x in found:
                return [i, found[x]]
            
            found[nums[i]] = i

        return []
