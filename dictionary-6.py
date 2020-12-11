# student results count in dictionary
students_rerult = {
    'Habib': {'Bangla': 75, 'English': 76, 'Math': 87, 'Programming': 89},
    'Tajbid': {'Bangla': 65, 'English': 66, 'Math': 87, 'Programming': 76},
    'Asif': {'Bangla': 95, 'English': 86, 'Math': 87, 'Programming': 78},
    'Rahman': {'Bangla': 85, 'English': 79, 'Math': 87, 'Programming': 67},
    'Anam': {'Bangla': 55, 'English': 76, 'Math': 87, 'Programming': 87},
    'Abdur': {'Bangla': 75, 'English': 76, 'Math': 87, 'Programming': 76},
}
# Particular keys access methods ---- student Habib
print(students_rerult['Habib']['Math'])
print(students_rerult['Habib'])
print(students_rerult)

# new keys and value add in dictionary---
students_rerult['Tamim'] = {'Bangla': 75, 'English': 86, 'Math': 87, 'Programming': 69}
print(students_rerult)

# Particular keys access methods ---- student Tamim
print(students_rerult['Tamim']['Math'])
print(students_rerult['Tamim'])
print(students_rerult)
