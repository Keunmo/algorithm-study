# https://leetcode.com/problems/majority-element/

def majorityElement(nums):
    if len(nums) == 1:
        print(nums[0])
        return nums[0]
    nums.sort()
    nums.append('End')
    print(nums)
    count = 1
    quantity = {}
    for i in range(len(nums)):
        if nums[i] == 'End':
            break
        elif nums[i]==nums[i+1]:
            count+=1
            quantity[nums[i]]=count
        else:
            count=1
    print("q:", quantity)
    quan_k = list(quantity.keys())
    # print("qk:", quan_k)
    quan_v = list(quantity.values())
    # print("qv:", quan_v)
    quan_v.sort()
    val = quan_v[-1]
    for k in quan_k:
        if quantity.get(k) == val:
            print(k)
            return k

majorityElement([2,2,1,1,1,2,2])


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        nums.append('End')
        count = 0
        lenth = len(nums)
        quantity = {}
        for i in range(lenth):
            if nums[i] == 'End':
                break
            elif nums[i]==nums[i+1]:
                count+=1
                quantity[nums[i]]=count
            else:
                count=1
        quan_k = list(quantity.keys())
        quan_v = list(quantity.values())
        quan_v.sort()
        val = quan_v[-1]
        for k in quan_k:
            if quantity.get(k) == val:
                return k