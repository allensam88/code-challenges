# https://leetcode.com/problems/contains-duplicate/
#
# <----Problem Statement----->
# Given an array of integers, find if the array contains any duplicates.

# ~~~Specifications~~~
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.


def duplicates(nums):
    # establish visited hash table set
    visited = set()

    # check each value in nums
    for i in nums:
        # if the value has already been seen, then it's a duplicate and return true
        if i in visited:
            return True

        # add the value to the visited hash table set
        visited.add(i)

    # after visiting all values, if no duplicates, return false
    return False
