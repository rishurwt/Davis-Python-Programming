nums = [1, 2, 2, 3]
frequency = {}
for n in nums:
        frequency[n] = frequency.get(n, 0) + 1
print(f"Output: {frequency}")