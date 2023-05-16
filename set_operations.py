# a =(2, "K")
# print(type(a))

# a1 = {"a": 20, "a":30, "b":30}
# print(type(a1))
# print(a1)
# print(len(a1))

a2 = {1,2,3,4}
b2 = {6,7,8,9, 10, 11, 2, 3}

new_intersection_a2b2 = a2.intersection(b2)
print(new_intersection_a2b2)

new_union_a2b2 = a2.union(b2)
print(new_union_a2b2)

new_difference_a2b2 = a2.difference(b2)
print(new_difference_a2b2)

diff_2 = b2.difference(a2)
print(diff_2)