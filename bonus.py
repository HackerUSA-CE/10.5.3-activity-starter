original_list = [1, 2, 3, 6, 7, 8]

def is_even(lst):
    return lst % 2 == 0

even_lst = list(filter(is_even, original_list))

print(even_lst)