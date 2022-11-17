# programme to remove the ith occurrence of the given word in a list where words can repeat.

l= ['list','python','java','list','tuple','java','c','list','string']
word_remove = 'java' # word to be removed from the list, this can be taken from the user by input
word_remove_occ = 2 # words occurrence to be removed, this can be taken from the user by input
count = 0
rev_l = []
for i in l:
    if i == word_remove:
        count += 1
        if count != word_remove_occ:
            rev_l.append(i)
    else:
        rev_l.append(i)
if count == 0:
    print("word not found")
else:
    print("List after removal:",rev_l)