# program to find common items in two list
c1 = ['red', 'green', 'blue']
c2 = ['pink', 'red', 'yellow', 'green']
print("Common elements in two lists are:",set(c1) & set(c2)) # &- is used for intersection

# same output can be produced by .intersection method of sets, which is shown below
print("Common elements", set(c1).intersection(set(c2)))