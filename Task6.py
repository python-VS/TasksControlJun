list_1 = [1, 5, 'text', [4, 6], 5.4]
list_2 = ['a', 2, 5.3, [3, 8], 'text', False, 1]
list_4 = []
for i in list_1:
    if i in list_2:
        list_4.append(i)
print(list_4)