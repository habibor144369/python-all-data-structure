# tuple in for loop use---
items = (12, 13, 14, 16, 18, [45, 67, 87, 96], ['habib', 'ar rahman', 'wahid'], ('hello', 'world', 'yeah'), {'name': 'Habibor Rahaman', 'id': 144369, 'phone': '01768280237'})
print(items[6],type(items[6]))
print(items[7],type(items[7]))
print(items[8],type(items[8]))

for items in items:
    print(items, type(items))
