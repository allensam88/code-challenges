# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:
# Input:
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
# Output: 4

# Example 2:
# Input:
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
# Output: -1


def search(nums, target):
    dict = {}

    for index in range(len(nums)):
        dict[nums[index]] = index

    return dict.get(target, -1)


print(search(nums1, target1))
print(search(nums2, target2))
