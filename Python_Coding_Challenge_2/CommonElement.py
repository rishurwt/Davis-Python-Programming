list1 = [1, 2, 3]
list2 = [2, 3, 4]

common = list(set(list1) & set(list2))
print(f"Output: {common}")