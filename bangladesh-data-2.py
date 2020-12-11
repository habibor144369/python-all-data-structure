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

# print(bangladesh_information) # print dictionary

# Particular key of keys print in dictionary---
All_Data = bangladesh_information['Dhaka'].keys()
print(All_Data)
# for loop Particular key of keys in dict_keys
for data in  All_Data:
    print(data)

# Particular key print in dictionary--
All_Data = bangladesh_information.keys()
print(All_Data)
# for loop using dict_keys
for information in  All_Data:
    print(information)

# for loop using dict_keys find out Uapazila----
for information in  All_Data:
    print(information, bangladesh_information[information]['Upazila'])


# direct dictionary on for loop using --- and find out keys and upazila count here---
for item in bangladesh_information:
    print(item, bangladesh_information[item]['Upazila'])

# direct dictionary on for loop using --- and find out keys and keys value---
for item in bangladesh_information:
    print(item, bangladesh_information[item])

# 2 nd methods here---
for keys, values in bangladesh_information.items():
    print(keys, values)

 # direct dictionary on for loop using --- and find out particular keys and keys value---
for keys, values in bangladesh_information['Dhaka'].items():
    print(keys, values)

print("Program Terminated here eye!")