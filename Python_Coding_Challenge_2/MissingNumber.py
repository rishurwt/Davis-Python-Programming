nums = [1, 2, 4, 5]
n = nums[-1] 
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
missing = expected_sum - actual_sum
print(f"Output: {missing}")