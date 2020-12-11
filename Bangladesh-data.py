# data of bangladesh
# its a empty dictionary----
bangladesh_information = {}

# data insert in empty dictionary
bangladesh_information['Dhaka'] = {'District': 13, 'Upazila': 93, 'UnionCouncil': 1833}
bangladesh_information['Chittagong'] = {'District': 11, 'Upazila': 97, 'UnionCouncil': 336}
bangladesh_information['Barisal'] = {'District': 6, 'Upazila': 39, 'UnionCouncil': 333}
bangladesh_information['Rangpur'] = {'District': 8, 'Upazila': 58, 'UnionCouncil': 536}
bangladesh_information['Khulna'] = {'District': 10, 'Upazila': 59, 'UnionCouncil': 270}
bangladesh_information['Mymensingh'] = {'District': 8, 'Upazila': 70, 'UnionCouncil': 350}
bangladesh_information['Rajshahi'] = {'District': 13, 'Upazila': 93, 'UnionCouncil': 558}
bangladesh_information['Sylhet'] = {'District': 4, 'Upazila': 38, 'UnionCouncil':334}

print(bangladesh_information) # print dictionary

# for loop using in dictionary--
for data in bangladesh_information:
    print(data, bangladesh_information[data])

# for loop using in dictionary and access Particular keys full dictionary---
for item in bangladesh_information:
    print(item, 'District :', bangladesh_information[item]['District'])

# its particular value access in dictionary--
print(bangladesh_information['Dhaka']['Upazila'])

# Particular key on for loop using in dictionary---
for item in bangladesh_information['Dhaka']:
    print(item, bangladesh_information['Dhaka'][item])



# this is ready dictionary
mama = {
    'Dhaka': {'District': 13, 'Upazila': 93, 'UnionCouncil': 1833},
    'Chittagong': {'District': 11, 'Upazila': 97, 'UnionCouncil': 336},
    'Barisal': {'District': 6, 'Upazila': 39, 'UnionCouncil': 333},
    'Rangpur': {'District': 8, 'Upazila': 58, 'UnionCouncil': 536},
    'Khulna': {'District': 10, 'Upazila': 59, 'UnionCouncil': 270},
    'Mymensingh': {'District': 8, 'Upazila': 70, 'UnionCouncil': 350},
    'Rajshahi': {'District': 13, 'Upazila': 93, 'UnionCouncil': 558},
    'Sylhet': {'District': 4, 'Upazila': 38, 'UnionCouncil': 334}
}

# for loop using in dictionary----
for i in mama:
    print(i, mama[i])

# for loop using in dictionary and access Particular keys full dictionary---
for item in mama:
    print(item, 'District :', mama[item]['District'])

# Particular key on for loop using in dictionary---
for N in mama['Rangpur']:
    print(N, mama['Rangpur'][N])

# for loop using dictionary---

n = {'District': 13, 'Upazila': 93, 'UnionCouncil': 1833}
for m in n:
    print(m, n[m])
