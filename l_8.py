# programme to count how many numbers are there in a list from a specific range

l = [10, 4, 5, 6, 7, 5, 6, 2, 5, 7, 2, 6, 5, 7, 10, 13, 5, 12, 7, 6, 8, 9, 6, 7876]
count =0
min_num = int(input("enter the minimum number"))
max_num = int(input("enter the maximum number"))
for i in l:
    if i in range(min_num, max_num):
        count += 1

print("Between", min_num, 'to', max_num, ',', count, 'numbers are present in list')
