# https://leetcode.com/problems/two-sum/

#  -----Problem Statement-----
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.


def twoSum(nums, target):
    # first pass solution O(n^2) really slow
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return i, j

    # optimized solution... using hash table dictionary
    nums_dict = {}
    for index in range(len(nums)):
        test = target - nums[index]

        if test in nums_dict:
            return nums_dict[test], index
        else:
            nums_dict[nums[index]] = index


nums = [2, 7, 11, 15]
print(twoSum(nums, 9))
