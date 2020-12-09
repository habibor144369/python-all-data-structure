# item remove in list use condition---input from user--
list = ['Mango', 'Banana', 'Orange','Avocado', 'Apple', 'Pineapple', 'Peach', 'Melon',]

item = input('Please select you item in list, and remove the item : ')

if item in list:
    list.remove(item)
    print(list)

else:
    print(item, 'not in list')

print('Program terminated!')
