# %%
#create a temporary cell
print('hello world')
numbers = [10, 25, 67, 89, 45, 89]

max_value = max(numbers)  # Get the maximum value
max_index = numbers.index(max_value)  # Get the index of the maximum value

print(f"Max Value: {max_value}, Index: {max_index}")
# %%
numbers = [10, 25, 67, 89, 45]

max_index, max_value = max(enumerate(numbers), key=lambda x: x[1])

print(f"Max Value: {max_value}, Index: {max_index}")
# Output: Max Value: 89, Index: 3
# %%
import numpy as np

numbers = np.array([10, 25, 67, 89, 45])

max_index = np.argmax(numbers)  # Index of max value
max_value = numbers[max_index]  # Max value

print(f"Max Value: {max_value}, Index: {max_index}")
# Output: Max Value: 89, Index: 3
# %%
numbers = [10, 25, 67, 89, 45, 89]

max_value = max(numbers)
max_indices = [i for i, num in enumerate(numbers) if num == max_value]

print(f"Max Value: {max_value}, Indices: {max_indices}")
# Output: Max Value: 89, Indices: [3, 5]
# %%
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    return candidate
# %%
nums = [3, 3, 3, 1, 2, 1, 4, 8]
print(majorityElement(nums))  # Output: 3

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))  # Output: 2
# %%
from collections import Counter

def majorityElement(nums):
    counts = Counter(nums)
    return max(counts.keys(), key=counts.get)
# %%
nums = [3, 3, 3, 1, 2, 1, 4, 8]
print(majorityElement(nums))  # Output: 3

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))  # Output: 2
# %%

nums = [3, 3, 3, 1, 2, 1, 4, 8]
counts = Counter(nums)
print(counts)
print(counts.get(1))
print(counts.keys())
# %%
