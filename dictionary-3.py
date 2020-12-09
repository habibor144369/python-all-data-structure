# dictionary data structure--
marks = {
    1:{'name': 'Habibor Rahaman', 'roll': 14, 'result':{'Bangla': {'first': {'sahitto': 77, 'kobita': 76}, 'second': 65}, 'English': 79, 'Programing': 98, 'Math': 92, 'Science': 80}},
    2:{'name': 'Abdullah', 'roll': 17, 'result':{'Bangla': 78, 'English': 79, 'Programing': 80, 'Math': 87, 'Science': 89}},
    3:{'name': 'Mohammodullah', 'roll': 13, 'result':{'Bangla': 74, 'English': 73, 'Programing': 90, 'Math': 85, 'Science': 84}},
    4:{'name': 'Wahidur rahman', 'roll': 23, 'result':{'Bangla': 77, 'English': 79, 'Programing': 60, 'Math': 78, 'Science': 89}},
    5:{'name': 'siyam', 'roll': 44, 'result':{'Bangla': 56, 'English': 79, 'Programing': 70, 'Math': 79, 'Science': 81}},
    6:{'name': 'soron', 'roll': 24, 'result':{'Bangla': 75, 'English': 76, 'Programing': 60, 'Math': 74, 'Science': 82}}
}
# particuler key access in dictionary--- simple 1 person data here
print(marks[1]['result']['Bangla']['first']['sahitto'])
print(marks[1]['result']['Bangla']['first'])
print(marks[1]['result']['Bangla'])
print(marks[1]['result'])
print(marks[1])
print(marks)

# particuler person key call----
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
print(marks[6])

# for loop use in dictionary ----
for i in marks:
    print(i, marks[i])
