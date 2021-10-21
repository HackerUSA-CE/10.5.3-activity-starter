# add code below for problem 3

lst = [1, 5, 7, 8, 9, 12]

alist = [x for x in lst]
print(alist)

blist = [x+3 for x in lst]
print(blist)

clist = [x+3 for x in lst if x < 10]
print(clist)
