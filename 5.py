# add code below for problem 5

original_list = [1, 5, 7]

def add3(a):
    return a + 3

new_list = list(map(add3, original_list))
print(new_list)

# using map with a lambda function
# new_list = list(map(lambda x: x+3, original_list))
# print(new_list)

# You can compare the above solutions with using list comprehension below
# original_list = [1, 5, 7, 8, 9, 10]
# new_list = [x+3 for x in original_list]
# print(new_list)