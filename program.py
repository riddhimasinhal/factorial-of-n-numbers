# Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
# A subarray is a contiguous non-empty sequence of elements within an array.
def maxSubArray (num):
    curr_sum=num[0]
    max_sum= num[0]
    for i in range(1, len(num)):
        curr_sum= max(num[i], curr_sum+num[i])
        max_sum = max(curr_sum, max_sum)
    return max_sum
num = list(map(int, input().split()))
print(maxSubArray(num))