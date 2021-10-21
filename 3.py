# add code below for problem 3

original_list = [1, 5, 7, 8, 9, 12]

alist = [x for x in original_list]
print(alist)

blist = [x+3 for x in original_list]
print(blist)

clist = [x+3 for x in original_list if x < 10]
print(clist)
