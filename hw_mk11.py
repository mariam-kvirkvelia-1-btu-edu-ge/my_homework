# task 1
def unique_list(lt):
    return set(lt)


print(unique_list([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9]))


# task 2
def immutable_set(lt):
    return frozenset(lt)


a = immutable_set([1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9])
print(a)


# task 3
def set_to_tuple(set1, set2):
    union_set = set1.union(set2)
    union_tuple = tuple(union_set)
    return union_tuple


tuplee = set_to_tuple({1, 2, 3, 4, 5, 6, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 8})

print(tuplee)
