# Programme to convert list of tuples into dictionary

l = [(3, 40), (2, 22), ('car', 'black'), ('year', 2012)]
new_dict = {i[0]: i[1] for i in l}
print("converted dictionary:",new_dict)