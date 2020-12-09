# list in list, dictionary, tuple----
item = [12, 45, 67, 89, (23, 56, 78,), ['hello', 'programmer', 'developer'], {'name': 'Habibor Rahaman', 'id': 144369, 'phone': '01768280237'}]
print(item[1], type(item[1]))
print(item[4], type(item[4]))
print(item[5], type(item[5]))
print(item[6], type(item[6]))

for items in item:
    print(items, type(items))
