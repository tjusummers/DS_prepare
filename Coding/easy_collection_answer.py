# %%
# Remove Duplicates from sorted non-decreasing Array
nums = [1,2,4,4,6,7,7]

def solution(nums):

    seen = nums[-1]
    n = len(nums)

    for i in range(n-2,-1,-1):
        if nums[i] == seen:
            nums.pop(i)
        else:
            seen = nums[i]

solution(nums)
print(nums)

# %%
# Best time to buy and sell stock II

#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
#However, you can buy it then immediately sell it on the same day.
#Find and return the maximum profit you can achieve.

prices = [1,4,7,9,10,4,2,7,4,5,8,6,3,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]

def solution(prices):
    profit = 0
    n = len(prices)
    for i in range(n-1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]
    return profit

maxprofit = solution(prices)
print(maxprofit)

# %%
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

nums1 = [0,0,2,4,0,0,0]
nums2 = [2,5,8]
m = len(nums1) - len(nums2)
n = len(nums2)
p1 = m - 1
p2 = n - 1
p = m + n - 1

while p2 >= 0:
    if p1 >= 0 and nums1[p1] > nums2[p2]:
        nums1[p] = nums1[p1]
        p1 -= 1
    else:
        nums1[p] = nums2[p2]
        p2 -= 1

    p -= 1

print(f'The result is: {nums1}')

# %%
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

from collections import Counter

def majorityElement(nums):
    counts = Counter(nums)
    return max(counts.keys(), key=counts.get)
# %%
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
nums = [1,2,3,4,5,6,3,2,1,7,8]
k = 3

n = len(nums)
a = [0] * n
for i in range(n):
    a[(i + k) % n] = nums[i]

nums[:] = a

print(nums)
# %%
