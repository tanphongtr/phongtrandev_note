import copy
# https://dzone.com/articles/a-comprehensive-guide-on-how-to-copy-objects-in-py
original_list = [1, 2, 3, [4, 5]]
copy_list = copy.deepcopy(original_list)

print("Original List: ", original_list)
print("Copy List: ", copy_list)

original_list[3][0] = 6
original_list[1] = 7

print("Original List: ", original_list)
print("Copy List: ", copy_list)