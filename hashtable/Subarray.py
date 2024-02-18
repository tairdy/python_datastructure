# Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).
# Your function should take two arguments:
# nums: a list of integers representing the input array
# target: an integer representing the target sum
# Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.


# WRITE SUBARRAY_SUM FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum - target in sum_index:
            print(
                f"answer found, current_sum={current_sum}, current_sum-target = {current_sum - target}, sum_index={sum_index[current_sum - target]+1}, {i} ")
            return [sum_index[current_sum - target] + 1, i]
        sum_index[current_sum] = i
        print(f"current sum_index = {sum_index}, current_sum = {current_sum}")
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))


nums = [-1, 2, 3, 5, 7, 11, 40]
target = 2
print(subarray_sum(nums, target))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
