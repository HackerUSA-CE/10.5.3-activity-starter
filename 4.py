# add code below for problem 4

def add(n):
    def increment(lst):
        new_list = []
        for i in lst:
            new_list.append(i + n)
        return new_list
    
    return increment

original_list = [1, 4, 6]

add3 = add(3)
print(add3(original_list))

add6 = add(6)
print(add6(original_list))

addNeg1 = add(-1)
print(addNeg1(original_list))