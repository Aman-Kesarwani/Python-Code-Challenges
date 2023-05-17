def tupleSum(tubleIterable):
    sum =0
    for item in tubleIterable:
        print(item)
        sum += item

    return sum

print("sum = {0}".format(tupleSum((12, 8, 2, 4 , 10))))

t1 = (1, 4, 6)
print(f"sum = {sum(t1)}")

a1, b1, c1 = t1
print(a1," " ,b1," ", c1)

t2 = (6, 8, 10)

t1, t2 = t2, t1

print(t1)
print(t2)


print(t2.index(4))




