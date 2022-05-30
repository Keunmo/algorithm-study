#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/submissions/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            result.append(i+1)
        result = set(result) - set(nums)
        return list(result)
