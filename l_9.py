# program to convert list of integers into a single integer

l = [10,22,38]
single_int = ''.join(list(map(str,l)))
print("Obtained single integer from list:", single_int)

# try by uncommenting the alternate solution given below.
# print("Obtained single integer from list:", ''.join([str(i) for i in l]))