#programme to swap the first and last element of a list
l = ['first', 34, 'data', 5, 'last']
print("original list is:",l)
l[0], l[-1] = l[-1], l[0]
print("after swapping list is:", l)