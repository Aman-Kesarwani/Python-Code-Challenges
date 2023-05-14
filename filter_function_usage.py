numbers = [2, 3, 5, 6, 7, 9, 12, 15, 18, 21, 24]

def filter_undivisble_by_3(number):
    if number %3 != 0:
        return number

filtered_by_function_list = list(filter(filter_undivisble_by_3, numbers))
print(filtered_by_function_list)

filtered_by_lambda_list = list(filter(lambda x: x%3 !=0, numbers))
print(filtered_by_lambda_list)