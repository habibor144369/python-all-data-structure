# item remove in list use condition---
list = ['Mango', 'Banana', 'Orange','Avocado', 'Apple', 'Pineapple', 'Peach', 'Melon',]
item = 'pineapple'

if item in list:
    list.remove(item)
    print(list)

else:
    print(item, 'not in list')

