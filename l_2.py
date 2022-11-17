#Program to remove duplicate elements from a list
l = [1,2,1,3,4,6,5,6,5]
# uncomment the below line ,incase you want list from user
# l = eval(input("Enter list of elements))
new_list = []
[new_list.append(i)for i in l if i not in new_list]
print("List without duplicate elements:",new_list)

       # OR uncomment the following alternate solution. But here the original sequence of elemments of list will not be followed.
# l = [1,2,1,30,4,6,5,6,5,34,30]
# rev_l = list(set(l))
# print(rev_l)