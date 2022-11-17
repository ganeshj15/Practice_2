# Programme to get the frequency of items in a list

l = [10, 77, 2, 6, 57, 10, 3, 5, 2, 77, 6, 8, 9, 6, 7876]
import collections
ctr = collections.Counter(l)
print('frequency of items:', ctr)