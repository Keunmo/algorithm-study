# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in nums:
            if i==0:
                del nums[nums.index(i)]
                nums.append(0)
        """
        Do not return anything, modify nums in-place instead.
        """
        