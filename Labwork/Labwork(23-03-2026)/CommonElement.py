list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [2, 5, 3]
common = set(list1) & set(list2) & set(list3)
result = list(common)
print(result)
