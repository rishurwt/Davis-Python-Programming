def get_evens(nums):
    return [x for x in nums if x % 2 == 0]
data = [1, 2, 3, 4]
print(f"Output: {get_evens(data)}")