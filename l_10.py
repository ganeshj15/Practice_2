#program to insert an element before each element of list.

l = [1,2,3,4]
print('original list:', l)
# suppose we want to add a 'ABC' before each item
rev_l = [i for elements in l for i in ('ABC',elements)]
print("modified list:", rev_l)