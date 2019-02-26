# 1、Two Sum
# description
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 方法一：
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target:
        #             a = i
        #             b = j

        # 方法二：
        # for i in range(len(nums)):
        #     if target-nums[i] in nums:
        #         b = nums.index(target-nums[i])
        #         a = i
        # 方法三：
        d = {}
        for index, num in enumerate(nums):
            d[index] = num
            another_num = target - num
            for key, value in d.items():
                if value == another_num:
                    a = index
                    b = list(d.keys())[list(d.values()).index(another_num)]
        return a, b


nums = [2, 7, 11, 15]
target = 22
f = Solution()
i1, j1 = f.twoSum(nums=nums, target=target)
print(i1, j1)


