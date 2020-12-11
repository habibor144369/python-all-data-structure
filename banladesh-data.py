#  data of bangladesh ---
bangladesh = {
  "Barisal":   ["Barguna",  "Barisal", "Bhola", "Jhalokati", "Patuakhali", "Pirojpur"],
  "Chittagong":["Bandarban","Brahmanbaria", "Chandpur", "Chittagong", "Comilla",    "Cox's Bazar","Feni", "Khagrachhari","Lakshmipur", "Noakhali", "Rangamati"],
  "Dhaka":     ["Dhaka",    "Faridpur", "Gazipur",  "Gopalganj",  "Kishoreganj","Madaripur",  "Manikganj","Munshiganj", "Narayanganj","Narsingdi","Rajbari","Shariatpur","Tangail"],
  "Khulna":    ["Bagerhat", "Chuadanga", "Jessore",  "Jhenaidah",  "Khulna",     "Kushtia",    "Magura",   "Meherpur", "Narail",     "Satkhira"],
  "Mymensingh":["Jamalpur", "Mymensingh", "Netrakona","Sherpur"],
  "Rajshahi"  :["Bogra",    "Chapainawabganj","Joypurhat","Naogaon",    "Natore",     "Pabna",      "Rajshahi", "Sirajganj"],
  "Rangpur"   :["Dinajpur", "Gaibandha", "Kurigram", "Lalmonirhat","Nilphamari", "Panchagarh", "Rangpur",  "Thakurgaon"],
  "Sylhet"    :["Habiganj", "Moulvibazar", "Sunamganj","Sylhet"]
}
# this particular key on for loop using in dictionary---
for i in bangladesh['Dhaka']:
  print(i)

# for looping in dictionary---
for i in bangladesh:
  print(i)  # dictionary all key here

# This is total dictionary on for loop using---
for x in bangladesh:
  print(x, bangladesh[x])   # now show all keys and there values of dictionary---


# This is total dictionary on for loop using---
for x in bangladesh:
  print(x, bangladesh[x][0])  # now show all keys and there 0 index values of dictionary---

# This is total dictionary on for loop using---
for x in bangladesh:
  print(x, bangladesh[x][0][2])   # now show all keys and there 0 index values 2 index string showing here of dictionary---

