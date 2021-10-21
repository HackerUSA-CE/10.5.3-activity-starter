# add code below for problem 1

def multiply(lst):
    new_list = []
    for n in lst:
        new_list.append(n*2)
    return new_list

numbers = [2, 4, 5, 10]
updated_numbers = multiply(numbers)
print(numbers)
print(updated_numbers)