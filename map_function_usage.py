numbers = [2, 4, 6, 8, 10]

def cube(x):
    return x**3

squared_numbers = list(map(lambda x: x**2, numbers))
cube_numbers = list(map(cube, numbers))
print("List: {0}".format(numbers))
print("Output map using labmda function- squared:{0}".format(squared_numbers))
print("Output map using normal function - cube:{0}".format(cube_numbers))