#  Programme to get a number from(1,20) randomly and append that into list.

# here we have to take help of random module

import random
random_numbers_list = []
n = int(input("enter no. of required elements"))
for i in range (n):
    random_numbers_list.append(random.randint(1,20))
print("List of random numbers:", random_numbers_list)
